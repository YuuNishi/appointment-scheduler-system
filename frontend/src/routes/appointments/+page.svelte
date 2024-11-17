<script lang="ts">
  import { onMount } from 'svelte';
  import moment from 'moment'
  import Sidebar from '../../components/sidebar/sidebar.svelte';
  import { get_appointments_by_range } from '../../services/appointment.service';
  import type {
    GetByRangeResponseType,
    GetByRangeType
  } from '../../types/services/appointment.types';
  import AppointmentCreate from '../../components/modals/appointment_modal/appointment_create.modal.svelte';
  import type { GetAllDoctorsType } from '../../types/services/doctor.types';
  import { get_all_doctors } from '../../services/doctor.service';
  import type { GetAllPatientType } from '../../types/services/patient.types';
  import { get_all_patients } from '../../services/patient.service';
  import AppointmentUpdate from '../../components/modals/appointment_modal/appointment_update.modal.svelte';
  import LoadingSpinner from '../../components/spinner/loading_spinner.svelte';
  
  let isDarkMode: boolean;
  let isLoading: boolean;

  let startDate = getStartOfWeek(new Date());
  let endDate = moment(startDate).add(6, 'days').toDate();
  let appointments: GetByRangeResponseType[] = [];

  onMount(() => {
    searchByRange();
  });

  function getStartOfWeek(date: Date): Date {
    const day = date.getDay();
    const diff = date.getDate() - day;
    return new Date(date.setDate(diff));
  }

  function formatDate(date: Date): string {
    return date.toLocaleDateString('pt-BR');
  }

  async function searchByRange(criteria?: any) {
    appointments = [];

    let data: GetByRangeType = {
      start_date: startDate,
      end_date: endDate,
      criteria: (criteria as HTMLInputElement)?.value
    };

    let result = await get_appointments_by_range(data);

    appointments = await result.json();
  }

  function goToPreviousWeek() {
    startDate.setDate(startDate.getDate() - 7);
    endDate.setDate(endDate.getDate() - 7);

    startDate = new Date(startDate);
    endDate = new Date(endDate);
    searchByRange();
  }

  function goToNextWeek() {
    startDate.setDate(startDate.getDate() + 7);
    endDate.setDate(endDate.getDate() + 7);

    startDate = new Date(startDate);
    endDate = new Date(endDate);
    searchByRange();
  }

  function isCorrectAppointment(
    appointment: GetByRangeResponseType,
    day: number,
    hour: number
  ): boolean {
    let currentAppointment = moment(appointment.date).add(
      appointment.start_time.substring(0, 2),
      'hours'
    );

    return currentAppointment.day() == day && currentAppointment.hour() == hour;
  }

  let doctors: GetAllDoctorsType[] = [];
  let patients: GetAllPatientType[] = [];

  async function executeAppointmentServices() {
    isLoading = true;

    await getAllDoctors();
    await getAllPatients();

    isLoading = false;
  }

  function handleModalSubmit() {
    searchByRange();
  }

  async function getAllDoctors() {
    doctors = [];

    let result = await get_all_doctors();

    doctors = await result.json();
  }

  async function getAllPatients() {
    patients = [];

    let result = await get_all_patients();

    patients = await result.json();
  }
</script>

<main>
  <Sidebar bind:isDarkMode />

  {#if (isLoading)}
    <LoadingSpinner />
  {/if}

  <div class="content {(isDarkMode && 'content-background-dark') || 'content-background-white'}">
    <div class="calendar-container">
      <nav class="navbar">
        <div class="navbar-content">
          <input
            class="form-control search"
            type="search"
            placeholder="Pesquisar pelo nome da consulta ou do paciente"
            aria-label="Search"
            on:keydown={(e) => e.key === 'Enter' && searchByRange(e.target)}
          />

          <div class="pagination me-auto">
            <button class="page-link" aria-label="Previous" on:click={goToPreviousWeek}
              >&laquo;</button
            >
            <span class="page-dates">{formatDate(startDate)} - {formatDate(endDate)}</span>
            <button class="page-link" aria-label="Next" on:click={goToNextWeek}>&raquo;</button>
          </div>

          <div class="buttons">
            <button
              data-bs-toggle="modal"
              data-bs-target="#appointmentCreate"
              type="button"
              class="btn new-appointment"
              on:click={executeAppointmentServices}>Nova Consulta</button
            >
            <AppointmentCreate on:submit={handleModalSubmit} bind:doctors bind:patients />
          </div>
        </div>
      </nav>

      <div class="calendar-header">
        {#each ['Dom.', 'Seg.', 'Ter.', 'Qua.', 'Qui.', 'Sex.', 'Sáb.'] as day, index}
          <div class="day-header">
            <span class="day-name">{day}</span>
            <span class="date">{moment(startDate).add(index, 'day').date()}</span>
          </div>
        {/each}
      </div>

      <div class="calendar-grid">
        {#each Array(7) as _, dayIndex}
          <div class="day-column">
            {#each Array(24) as _, hourIndex}
              <div class="time-slot" style="position: relative;">
                <span class="side-time">{moment(moment().date()).hour(hourIndex).format('H:mm')}</span>
                {#each appointments as appointment}
                  {#if isCorrectAppointment(appointment, dayIndex, hourIndex)}
                    <div on:click={executeAppointmentServices} data-bs-toggle="modal" data-bs-target="#appointmentUpdate" class="event {appointment.paid ? 'event-paid' : 'event-pending'}">{appointment.title}<br>{appointment.start_time} - {appointment.finish_time}</div>
                    <AppointmentUpdate on:submit={handleModalSubmit} currentAppointmentId={appointment.id} bind:doctors bind:patients />
                  {/if}
                {/each}
              </div>
            {/each}
          </div>
        {/each}
      </div>
    </div>
  </div>
</main>

<style>
  .calendar-container {
    width: 90%;
    margin: 0 auto;
    background-color: #f4f4f4;
    border: 1px solid #ddd;
    padding: 20px;
    border-radius: 8px;
  }

  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
  }

  .navbar-content {
    display: flex;
    align-items: center;
    width: 100%;
  }

  .search {
    width: 30%;
    margin-right: 15px;
  }

  .pagination {
    display: flex;
    align-items: center;
  }

  .page-dates {
    margin: 0 10px;
    font-weight: bold;
  }

  .buttons .btn {
    margin-left: 10px;
    padding: 6px 12px;
    font-size: 14px;
  }

  .new-appointment {
    background-color: #28a745;
    color: #fff;
  }

  .event-paid {
      border-left: 3px solid #0056b3;
  }

  .event-pending {
      border-left: 3px solid red;
  }

  .event {
      cursor: pointer;
      position: absolute;
      top: 20%;
      left: 5%;
      width: 90%;
      background-color: #e6f7ff;
      color: #0056b3;
      padding: 5px;
      font-size: 12px;
      border-radius: 4px;
  }

  .event:hover {
      background-color: #a4dbf5;
  }

  .calendar-header {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    margin-top: 10px;
    border-bottom: 1px solid #ddd;
  }

  .day-header {
    text-align: center;
    padding: 10px 0;
    font-weight: bold;
  }

  .day-name {
    display: block;
    font-size: 14px;
  }

  .date {
    display: block;
    font-size: 18px;
  }

  .calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    border-top: 1px solid #ddd;
  }

  .day-column {
    border-right: 1px solid #ddd;
    position: relative;
  }

  .time-slot {
    height: 60px;
    border-bottom: 1px solid #ddd;
  }

  .side-time {
    position: absolute;
    top: 0;
    right: 0;
    font-size: 6px;
    color: #555;
    width: 40px;
    text-align: right;
  }

  .calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    max-height: 600px;
    overflow-y: scroll;
    border-top: 1px solid #ddd;
  }
</style>
