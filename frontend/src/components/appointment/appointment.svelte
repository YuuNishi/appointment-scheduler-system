<script lang="ts">
    import type { GetByRangeResponseType } from "../../types/services/appointment.types";

  let appointmentInfo: GetByRangeResponseType;

  export { appointmentInfo }
</script>

<div class="event {appointmentInfo.paid ? 'event-pending' : 'event-paid'}">{appointmentInfo.title}<br>{appointmentInfo.start_time} - {appointmentInfo.finish_time}</div>

<style>
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
</style>