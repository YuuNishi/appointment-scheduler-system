<script lang="ts">
  import 'iconify-icon';
  import type { CreateDoctorType } from '../../../types/services/doctor.types';
  import ErrorToast from '../../toast/error_toast.svelte';
  import SuccessToast from '../../toast/success_toast.svelte';
  import { createEventDispatcher } from 'svelte';
  import type { CreateSpecialtyType, GetSpecialtyType } from '../../../types/services/specialty.types';
  import { create_doctor } from '../../../services/doctor.service';
  import { create_specialty } from '../../../services/specialty.service';

  const dispatch = createEventDispatcher();

  let showErrorToast: boolean;
  let toastError: string;

  let showSuccessToast: boolean;
  let toastSuccess: string;

  let specialties: GetSpecialtyType[] = [];

  export { specialties };

  let doctorName: string;
  let specialtyId: number;

  let isNewSpecialty: boolean = false;
  let doctorNewSpecialty: string;

  let isFormValid: boolean;

  function validateForm() {
    isFormValid = !!(
      doctorName &&
      ((!isNewSpecialty && specialtyId) || (isNewSpecialty && doctorNewSpecialty))
    );
  }

  async function handleSubmit() {
    if (!validateInput()) return;

    if (isNewSpecialty) {
      const specialtyData: CreateSpecialtyType = {
        description: doctorNewSpecialty
      };

      let data = await create_specialty(specialtyData);

      if (data.ok) {
        let dataJson: GetSpecialtyType = await data.json();
        specialtyId = dataJson.id;
      }
      else {
        showToast(0, 'Ocorreu um erro ao criar a especialidade');
        return;
      }
    }

    const doctorData: CreateDoctorType = {
      name: doctorName,
      speciality_id: specialtyId
    };

    try {
      let data = await create_doctor(doctorData);

      if (data.ok) {
        dispatch('submit', { success: true });
        showToast(1, 'Médico Criado com Sucesso');
      }
      else {
        throw new Error();
      }
    } catch {
      showToast(0, 'Ocorreu um erro ao criar médico. Por favor, tente novamente.');
      dispatch('submit', { success: false });
    }
  }

  function validateInput(): boolean {
    if (doctorName.length < 1) {
      showToast(0, 'O nome do médico deve ter pelo menos 1 caractere');
      return false;
    }

    if (isNewSpecialty && specialties.filter(specialty => specialty.description == doctorNewSpecialty).length > 0) {
      showToast(0, 'Especialidade já existente');
      return false;
    }

    if (isNewSpecialty && (doctorNewSpecialty.length < 10 || doctorNewSpecialty.length > 50)) {
      showToast(0, 'Especialidade deve possuir entre 10 a 50 caracteres');
      return false;
    }

    return true;
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

<div
  class="modal fade"
  id="doctorCreate"
  data-bs-backdrop="static"
  data-bs-keyboard="false"
  tabindex="-1"
  aria-labelledby="doctorCreateLabel"
  aria-hidden="true"
>
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title fs-5" id="doctorCreateLabel">Novo Especialista</h2>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar"
        ></button>
      </div>

      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="doctorTitle" class="form-label">Nome do médico</label>
            <input
              type="text"
              class="form-control"
              id="doctorTitle"
              placeholder="Digite o nome do especialista"
              bind:value={doctorName}
              on:input={validateForm}
            />
          </div>

          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <label class="input-group-text" for="specialtyType">
                <iconify-icon icon="maki:doctor" width="26" height="26" />
              </label>
            </div>
            <select
              class="custom-select form-select"
              id="specialtyType"
              bind:value={specialtyId}
              on:change={validateForm}
            >
              <option selected value="" disabled>Selecione a especialidade</option>
              {#each specialties as specialty}
                <option value={specialty.id}>{specialty.description}</option>
              {/each}
            </select>
          </div>

          <div class="form-check">
            <input
              class="form-check-input"
              type="checkbox"
              id="specialtyCheck"
              bind:checked={isNewSpecialty}
              on:change={validateForm}
            />
            <label class="form-check-label" for="specialtyCheck"> Criar especialidade </label>
          </div>

          <div class="mb-3">
            <label for="doctorNewSpecialty" class="form-label">Nome da especialidade</label>
            <input
              type="text"
              class="form-control"
              id="doctorNewSpecialty"
              placeholder="Digite o nome da especialidade"
              bind:value={doctorNewSpecialty}
              on:input={validateForm}
              disabled={!isNewSpecialty}
            />
          </div>
        </form>
      </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal"
          >Cancelar</button
        >
        <button
          type="button"
          class="btn btn-primary"
          data-bs-dismiss="modal"
          on:click={handleSubmit}
          disabled={!isFormValid}>Criar</button
        >
      </div>
    </div>
  </div>
</div>

<ErrorToast bind:showErrorToast bind:toastError />
<SuccessToast bind:showSuccessToast bind:toastSuccess />
