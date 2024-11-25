<script lang="ts">
  let showSuccessToast = false;
  let toastSuccess: string;

  export { showSuccessToast, toastSuccess }
</script>

<div class="position-fixed bottom-0 start-50 translate-middle-x p-3" style="z-index: 1060">
  <div class="toast align-items-center text-bg-success border-0 {showSuccessToast ? 'show' : ''}" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="d-flex">
      <div class="toast-body">
        { toastSuccess }
      </div>
      <button type="button" class="btn-close btn-close-white me-2 m-auto" aria-label="Close" on:click={() => showSuccessToast = false}></button>
    </div>
  </div>
</div>
