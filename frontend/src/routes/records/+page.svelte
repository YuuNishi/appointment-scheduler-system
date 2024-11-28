<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from '../../components/sidebar/sidebar.svelte';
  import type { GetAllPatientType } from '../../types/services/patient.types';
  import { get_all_patients, remove_patient } from '../../services/patient.service';
  import LoadingSpinner from '../../components/spinner/loading_spinner.svelte';
  import { isDarkTheme } from '../../store/theme.store';
  import Edit from '../edit/+page.svelte';
  import ErrorToast from '../../components/toast/error_toast.svelte';
  import SuccessToast from '../../components/toast/success_toast.svelte';
  import Breadcrumb from '../../components/breadcrumb/breadcrumb.svelte';
  import type { BreadCrumbItemType } from '../../types/services/shared.types';

  let patients: GetAllPatientType[] = [];

  export let showModal = false;

  let breadCrumbItems: BreadCrumbItemType[] = [
    {
      route: '/records',
      title: 'prontuários',
      active: true
    }
  ];

  let isLoading: boolean;

  let showErrorToast: boolean;
  let toastError: string;

  let showSuccessToast: boolean;
  let toastSuccess: string;

  let modalData;

  function toggleModal(data) {
    modalData = data;
    showModal = !showModal;
  }

  onMount(() => {
    getAllPatients();
  });

  $: if (!showModal) {
    getAllPatients();
  }

  function search() {
    let input, filter, table, tr, td, td2, i, txtValue, txtValue2;
    input = document.getElementById('inputdefault');
    filter = input.value.toUpperCase();
    table = document.getElementById('tb_patients');
    tr = table.getElementsByTagName('tr');

    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName('td')[0];
      td2 = tr[i].getElementsByTagName('td')[1];
      if (td) {
        txtValue = td.textContent || td.innerText;
        txtValue2 = td2.textContent || td2.innerText;
        if (
          txtValue.toUpperCase().indexOf(filter) > -1 ||
          txtValue2.toUpperCase().indexOf(filter) > -1
        ) {
          tr[i].style.display = '';
        } else {
          tr[i].style.display = 'none';
        }
      }
    }
  }

  async function getAllPatients() {
    isLoading = true;

    patients = [];

    try {
      let result = await get_all_patients();

      if (result.ok) {
        patients = await result.json();
        patients.reverse();
      } else {
        throw new Error();
      }
    } catch {
      showToast(0, 'Erro ao consultar os prontuários');
    } finally {
      isLoading = false;
    }
  }

  let isSorted = false;
  function sortTable() {
    if (!isSorted) {
      patients = patients.sort((a, b) => a.name.localeCompare(b.name));
    } else {
      patients = patients.sort((a, b) => b.name.localeCompare(a.name));
    }

    isSorted = !isSorted;
  }

  async function onClickDelete(id: number) {
    await deletePatient(id);
    await getAllPatients();
  }

  async function deletePatient(id: number) {
    isLoading = true;

    try {
      const patientResponse = await remove_patient(id);

      if (patientResponse.ok) {
        showToast(1, 'Paciente removido com sucesso');
      } else {
        throw new Error();
      }
    } catch {
      showToast(0, 'Erro ao deletar paciente');
    } finally {
      isLoading = false;
    }
  }

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
</script>

<main>
  <Sidebar />

  {#if isLoading}
    <LoadingSpinner />
  {/if}

  <div class="content {($isDarkTheme && 'content-background-dark') || 'content-background-white'}">
    <Breadcrumb {breadCrumbItems} />
    <h1 class={$isDarkTheme && 'text-white'}>Prontuários</h1>

    <div class="form-group">
      <input
        class="form-control"
        id="inputdefault"
        type="text"
        placeholder="Digite o nome ou CPF"
        on:keyup={search}
      />
    </div>

    <div class="results">
      <div class="text-right">
        <button class="btn control" on:click={() => sortTable()}>
          <iconify-icon icon="bi:filter" width="1.8em" height="1.8em" class="icon"></iconify-icon>
        </button>
        <a href="/register">
          <button class="btn btn-success control">Novo Paciente</button>
        </a>
      </div>

      <table class="table" id="tb_patients">
        <thead>
          <tr>
            <th scope="col">Nome</th>
            <th scope="col">CPF</th>
            <th scope="col">Sexo</th>
            <th scope="col">Data de nascimento</th>
            <th scope="col"></th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {#each patients as person}
            <tr>
              <td>{person.name}</td>
              <td>{person.cpf}</td>
              {#if person.sex == 1}
                <td>Feminino</td>
              {:else}
                <td>Masculino</td>
              {/if}
              <td>{person.birth_date}</td>
              <td>
                <button class="btn btn-default" on:click={() => toggleModal({ person })}>
                  <iconify-icon
                    icon="subway:pencil"
                    width="1.2em"
                    height="1.2em"
                    class="icon icon-edit"
                  ></iconify-icon>
                </button>
              </td>
              <td>
                <button
                  class="btn btn-default"
                  on:click={() => {
                    onClickDelete(person.id);
                  }}
                >
                  <iconify-icon
                    icon="material-symbols:delete"
                    width="1.2em"
                    height="1.2em"
                    class="icon icon-edit"
                  ></iconify-icon>
                </button>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
    {#if showModal}
      <Edit on:click={toggleModal} bind:values={modalData} bind:show={showModal} />
    {/if}
  </div>
</main>

<ErrorToast bind:showErrorToast bind:toastError />
<SuccessToast bind:showSuccessToast bind:toastSuccess />

<style>
  main {
    display: flex;
  }
  .control {
    float: right;
    margin: 1%;
  }
  .icon {
    color: rgb(61, 152, 255);
  }
  .results {
    margin-top: 1rem;
    background-color: #ffffff;
    padding-top: 2rem;
  }
  .icon-edit {
    align-self: right;
    cursor: pointer;
  }
</style>
