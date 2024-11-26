<script lang="ts">
  import LoadingSpinner from '../../../components/spinner/loading_spinner.svelte';
  import Sidebar from '../../../components/sidebar/sidebar.svelte';
  import { isDarkTheme } from '../../../store/theme.store';
  import ErrorToast from '../../../components/toast/error_toast.svelte';
  import SuccessToast from '../../../components/toast/success_toast.svelte';
  import Breadcrumb from '../../../components/breadcrumb/breadcrumb.svelte';
  import type { BreadCrumbItemType } from '../../../types/services/shared.types';
  import type { GetAllDoctorsType } from '../../../types/services/doctor.types';
  import 'iconify-icon';
  import { get_all_specialties } from '../../../services/specialty.service';
  import type { GetSpecialtyType } from '../../../types/services/specialty.types';
  import DoctorCreate from '../../../components/modals/doctor_modal/doctor_create.modal.svelte';
  import { delete_doctor, get_all_doctors } from '../../../services/doctor.service.js';

  export let data;

  let doctors: GetAllDoctorsType[] = data.doctors;
  let specialties: GetSpecialtyType[] = [];

  let showErrorToast: boolean;
  let toastError: string;

  let showSuccessToast: boolean;
  let toastSuccess: string;

  let breadCrumbItems: BreadCrumbItemType[] = [
    {
      route: '/settings',
      title: 'configurações',
      active: false
    },
    {
      route: '/settings/doctors',
      title: 'profissionais',
      active: true
    }
  ];

  let isLoading: boolean;

  function showToast(type: number, message: string) {
    if (type == 0) {
      toastError = message;
      showErrorToast = true;
    }
    if (type == 1) {
      toastSuccess = message;
      showSuccessToast = true;
    }
  }

  async function deleteDoctor(id: string) {
    try {
      let data = await delete_doctor(id);

      if (data.ok) {
        showToast(1, 'Médico deletado com sucesso.');
      } else {
        throw new Error();
      }
    } catch {
      showToast(0, 'Erro inesperado ao deletar o médico.');
    } finally {
      await executeDoctorServices();
    }
  }

  async function executeDoctorServices() {
    isLoading = true;

    await getAllSpecialties();
    await getAllDoctors();

    isLoading = false;
  }

  async function getAllSpecialties() {
    specialties = [];

    let result = await get_all_specialties();

    specialties = await result.json();
  }

  async function getAllDoctors() {
    doctors = [];

    let result = await get_all_doctors();

    doctors = await result.json();
  }
</script>

<main>
  <Sidebar />

  {#if isLoading}
    <LoadingSpinner />
  {/if}

  <div class="content {$isDarkTheme && 'text-white'} {($isDarkTheme && 'content-background-dark') || 'content-background-white'}">
    <Breadcrumb {breadCrumbItems} />

    <h1>Configurações de profissionais</h1>

    <div class="d-flex justify-content-end">
      <button
        data-bs-toggle="modal"
        data-bs-target="#doctorCreate"
        type="button"
        class="btn btn-success my-2"
        on:click={executeDoctorServices}
        >Novo Especialista
      </button>
      <DoctorCreate on:submit={executeDoctorServices} bind:specialties />
    </div>

    {#if doctors.length == 0}
      <span>Nenhum médico encontrado</span>
    {/if}

    {#if doctors.length > 0}
      <table class="table {$isDarkTheme && 'table-dark'}">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Nome</th>
            <th scope="col">Especialidade</th>
            <th scope="col">Excluir</th>
          </tr>
        </thead>
        <tbody>
          {#each doctors as doctor, index}
            <tr>
              <th scope="row">{index + 1}</th>
              <td>{doctor.name}</td>
              <td>{doctor.specialty}</td>
              <td>
                <button
                  class="btn btn-danger btn-delete d-flex align-items-center justify-content-center"
                  on:click={() => deleteDoctor(doctor.id)}
                >
                  <iconify-icon icon="game-icons:trash-can" width="1.2rem" height="1.2rem" />
                </button>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    {/if}
  </div>
</main>

<ErrorToast bind:showErrorToast bind:toastError />
<SuccessToast bind:showSuccessToast bind:toastSuccess />

<style>
  .btn-delete {
    height: 2rem;
    width: 2rem;
  }
</style>
