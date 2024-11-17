<script lang="ts">
  import 'iconify-icon';
    import type { GetAllDoctorsType } from '../../../types/services/doctor.types';
    import type { GetAllPatientType } from '../../../types/services/patient.types';
    import type { CreateAppointment } from '../../../types/services/appointment.types';
    import moment from 'moment';
    import ErrorToast from '../../toast/error_toast.svelte';
    import { create_appointment } from '../../../services/appointment.service';

  let showErrorToast: boolean;
  let toastError: string;

  let doctors: GetAllDoctorsType[] = []; 
  let patients: GetAllPatientType[] = [];

  export { doctors, patients }


  let appointmentTitle: string;
  let appointmentType: number;
  let professionalId: number;
  let patientId: number;
  let dateTime: string;
  let finishTime: number;

  let isFormValid: boolean;

  function validateForm() {
    isFormValid = !!(appointmentTitle && appointmentType && professionalId && patientId && dateTime && finishTime);
  }

  async function handleSubmit() {
    if (!validateInput())
      return;

    const appointmentData: CreateAppointment = {
      title: appointmentTitle,
      type: appointmentType,
      created_by: 'mock-user12344',
      doctor_ids: [
        professionalId
      ],
      patient_id: patientId,
      date: moment(dateTime).format('yyyy-MM-DD'),
      start_time: moment(dateTime).format('HH:mm:ss'),
      finish_time: moment(dateTime).add(finishTime, 'minute').format('HH:mm:ss')
    };

    try {
      await create_appointment(appointmentData);
    }
    catch {
      showToast(0, "Ocorreu um erro ao criar a consulta. Por favor, tente novamente.");
    }
  }

  function validateInput(): boolean {
    if (appointmentTitle.length < 10) {
      showToast(0, "O nome da consulta deve ter pelo menos 10 caracteres");
      return false;
    }

    if (finishTime > 120) {
      showToast(0, "A duração da consulta não pode ultrapassar 120 minutos");
      return false;
    }

    return true;
  }

  function showToast(type: number, message: string) {
    if (type == 0) {
      toastError = message;
      showErrorToast = true;
    }
  }
</script>

<div
  class="modal fade"
  id="appointmentCreate"
  data-bs-backdrop="static"
  data-bs-keyboard="false"
  tabindex="-1"
  aria-labelledby="appointmentCreateLabel"
  aria-hidden="true"
>
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title fs-5" id="appointmentCreateLabel">Nova Consulta</h2>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar"
        ></button>
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
              <option selected value="" disabled>Selecione o tipo de agendamento</option>
              <option value=0>Exame de rotina</option>
              <option value=1>Consulta de especialista</option>
              <option value=2>Consulta de emergência</option>
              <option value=3>Consulta de retorno</option>
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
              <option selected value="" disabled>Selecione o profissional</option>
              {#each doctors as doctor}
                <option value="{doctor.id}">{doctor.name}</option>
              {/each}
            </select>
          </div>

          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <label class="input-group-text" for="appointmentType">
                <iconify-icon icon="ic:sharp-person" width="26" height="26" />
              </label>
            </div>
            <select class="form-select" id="patient"
              bind:value={patientId}
              on:input={validateForm}
            >
              <option selected value="" disabled>Selecione o paciente</option>
              {#each patients as patient}
                <option value="{patient.id}">{patient.name}</option>
              {/each}
            </select>
          </div>

          <div class="mb-3">
            <label for="dateTime" class="form-label"
              ><i class="bi bi-calendar"></i> Data e Hora da consulta</label
            >
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
        <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal"
          >Cancelar</button
        >
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal"  on:click={handleSubmit} disabled={!isFormValid}>Criar</button>
      </div>
    </div>
  </div>
</div>

<ErrorToast bind:showErrorToast bind:toastError />