<div class="loading-overlay">
  <div class="loading-spinner d-flex flex-column justify-content-center align-items-center">
    <div class="spinner-border text-primary" role="status" />
    <span>Carregando...</span>
  </div>
</div>

<style>
    .loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(255, 255, 255, 0.01);
        backdrop-filter: blur(2px);
        z-index: 9999;
        pointer-events: all;
    }

    .loading-spinner {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        pointer-events: none;
    }
</style>
