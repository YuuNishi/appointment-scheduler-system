<script lang="ts">
  let showErrorToast = false;
  let toastError: string;

  export { showErrorToast, toastError }
</script>

<div class="position-fixed bottom-0 start-50 translate-middle-x p-3" style="z-index: 1060">
  <div class="toast align-items-center text-bg-danger border-0 {showErrorToast ? 'show' : ''}" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="d-flex">
      <div class="toast-body">
        { toastError }
      </div>
      <button type="button" class="btn-close btn-close-white me-2 m-auto" aria-label="Close" on:click={() => showErrorToast = false}></button>
    </div>
  </div>
</div>
