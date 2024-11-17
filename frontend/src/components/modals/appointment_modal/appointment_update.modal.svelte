<script lang="ts">
  import { onDestroy, onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';
  import 'iconify-icon';
  import moment from 'moment';
  import ErrorToast from '../../toast/error_toast.svelte';
  import { delete_appointment, get_appointment_by_id, update_appointment } from '../../../services/appointment.service';
  import type { GetAllDoctorsType } from '../../../types/services/doctor.types';
  import type { GetAllPatientType } from '../../../types/services/patient.types';
  import type { GetByIdResponseType, UpdateAppointment } from '../../../types/services/appointment.types';

  const dispatch = createEventDispatcher();

  let modalElement: HTMLElement;

  let showErrorToast: boolean;
  let toastError: string;

  let currentAppointmentId: number;
  let currentAppointment: GetByIdResponseType;

  let doctors: GetAllDoctorsType[] = [];
  let patients: GetAllPatientType[] = [];

  export { doctors, patients, currentAppointmentId };

  let appointmentTitle: string = '';
  let appointmentType: number;
  let paidType: number;
  let professionalId: number;
  let patientId: number;
  let dateTime: string;
  let finishTime: number;

  let isFormValid: boolean;

  function validateForm() {
    isFormValid = !!(
      appointmentTitle &&
      appointmentType != null &&
      professionalId != null &&
      patientId != null &&
      dateTime &&
      finishTime &&
      paidType != null
    );
  }

  async function handleSubmit() {
    if (!validateInput()) return;

    const appointmentData: UpdateAppointment = {
      title: appointmentTitle,
      type: appointmentType,
      paid: paidType,
      doctor_ids: [professionalId],
      patient_id: patientId,
      date: moment(dateTime).format('YYYY-MM-DD'),
      start_time: moment(dateTime).format('HH:mm:ss'),
      finish_time: moment(dateTime).add(finishTime, 'minutes').format('HH:mm:ss'),
    };

    try {
      await update_appointment(currentAppointmentId, appointmentData);
      dispatch('submit', { success: true });
    } catch {
      showToast(0, 'Ocorreu um erro ao atualizar a consulta. Por favor, tente novamente.');
      dispatch('submit', { success: false });
    }
  }

  async function handleDelete() {
    try {
      await delete_appointment(currentAppointmentId);
      dispatch('submit', { success: true });
    } catch {
      showToast(0, 'Ocorreu um erro ao deletar a consulta. Por favor, tente novamente.');
      dispatch('submit', { success: false });
    }
  }

  function validateInput(): boolean {
    if (appointmentTitle.length < 10) {
      showToast(0, 'O nome da consulta deve ter pelo menos 10 caracteres.');
      return false;
    }

    if (finishTime > 120) {
      showToast(0, 'A duração da consulta não pode ultrapassar 120 minutos.');
      return false;
    }

    return true;
  }

  function showToast(type: number, message: string) {
    if (type === 0) {
      toastError = message;
      showErrorToast = true;
    }
  }

  async function executeAppointmentGet() {
    try {
      let result = await get_appointment_by_id(currentAppointmentId);
      currentAppointment = await result.json();

      appointmentTitle = currentAppointment.title;
      appointmentType = currentAppointment.type;
      paidType = currentAppointment.paid;
      professionalId = currentAppointment.doctor_ids[0];
      patientId = currentAppointment.patient_id;
      dateTime = moment(`${currentAppointment.date}T${currentAppointment.start_time}`).format('YYYY-MM-DDTHH:mm:ss');
      finishTime = currentAppointment.duration;
    }
    catch {
      showToast(0, 'Ocorreu um erro ao buscar a consulta. Por favor, tente novamente.');
    }

    validateForm();
  }

  onMount(() => {
    modalElement.addEventListener('shown.bs.modal', executeAppointmentGet);
  });

  onDestroy(() => {
    modalElement.removeEventListener('shown.bs.modal', executeAppointmentGet);
  });
</script>

<div
  class="modal fade"
  id="appointmentUpdate"
  data-bs-backdrop="static"
  data-bs-keyboard="false"
  tabindex="-1"
  aria-labelledby="appointmentUpdateLabel"
  aria-hidden="true"
  bind:this={modalElement}
>
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title fs-5" id="appointmentUpdateLabel">Editar Consulta</h2>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar"></button>
      </div>

      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="appointmentTitle" class="form-label">Nome da Consulta</label>
            <input
              type="text"
              class="form-control"
              id="appointmentTitle"
              placeholder="Digite o nome da consulta"
              bind:value={appointmentTitle}
              on:input={validateForm}
            />
          </div>

          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <label class="input-group-text" for="appointmentType">
                <iconify-icon icon="raphael:calendar" width="26" height="26" />
              </label>
            </div>
            <select class="custom-select form-select" id="appointmentType"
                    bind:value={appointmentType}
                    on:input={validateForm}
            >
              <option value="" disabled>Selecione o tipo de agendamento</option>
              <option value={0}>Exame de rotina</option>
              <option value={1}>Consulta de especialista</option>
              <option value={2}>Consulta de emergência</option>
              <option value={3}>Consulta de retorno</option>
            </select>
          </div>

          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <label class="input-group-text" for="professional">
                <iconify-icon icon="fontisto:doctor" width="26" height="26" />
              </label>
            </div>
            <select class="custom-select form-select" id="professional"
                    bind:value={professionalId}
                    on:input={validateForm}
            >
              <option value="" disabled>Selecione o profissional</option>
              {#each doctors as doctor}
                <option value={doctor.id}>{doctor.name}</option>
              {/each}
            </select>
          </div>

          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <label class="input-group-text" for="patient">
                <iconify-icon icon="ic:sharp-person" width="26" height="26" />
              </label>
            </div>
            <select class="form-select" id="patient"
                    bind:value={patientId}
                    on:input={validateForm}
            >
              <option value="" disabled>Selecione o paciente</option>
              {#each patients as patient}
                <option value={patient.id}>{patient.name}</option>
              {/each}
            </select>
          </div>

          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <label class="input-group-text" for="payment">
                <iconify-icon icon="ion:card-outline" width="26" height="26" />
              </label>
            </div>
            <select class="form-select" id="payment"
                    bind:value={paidType}
                    on:input={validateForm}
            >
              <option value="" disabled>Status do pagamento</option>
              <option value={0}>Pagamento Pendente</option>
              <option value={1}>Pagamento Realizado</option>
            </select>
          </div>

          <div class="mb-3">
            <label for="dateTime" class="form-label"><i class="bi bi-calendar"></i> Data e Hora da consulta</label>
            <input type="datetime-local" class="form-control" id="dateTime"
                   bind:value={dateTime}
                   on:input={validateForm}
            />
          </div>

          <div class="mb-3">
            <label for="appointmentTime" class="form-label">Duração da consulta (em minutos)</label>
            <input
              type="number"
              class="form-control"
              id="appointmentTime"
              placeholder="Digite a duração da consulta"
              bind:value={finishTime}
              on:input={validateForm}
            />
          </div>
        </form>
      </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-outline-danger ms-2" data-bs-dismiss="modal" on:click={handleDelete}>
          <iconify-icon icon="game-icons:trash-can" width="1.2rem" height="1.2rem"/>
        </button>
        <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal">Cancelar</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" on:click={handleSubmit} disabled={!isFormValid}>Salvar</button>
      </div>
    </div>
  </div>
</div>

<ErrorToast bind:showErrorToast bind:toastError />
