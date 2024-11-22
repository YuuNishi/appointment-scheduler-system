<script lang="ts">
  import LoadingSpinner from '../../components/spinner/loading_spinner.svelte';
  import Sidebar from '../../components/sidebar/sidebar.svelte';
  import { isDarkTheme } from '../../store/theme.store';

  let isLoading: boolean;
</script>

<main>
  <Sidebar />

  {#if (isLoading)}
    <LoadingSpinner />
  {/if}

  <div class="content {($isDarkTheme && 'content-background-dark') || 'content-background-white'}">
    <h1 class="mb-3">Configurações</h1>

    <div class="d-flex gap-2">
      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Configurações de Usuário</h5>
          <p class="card-text">Alterar avatar, nome de usuário e senha.</p>
          <a href="/settings/user" class="btn btn-primary">Acessar</a>
        </div>
      </div>

      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Configurações de Profissionais</h5>
          <p class="card-text">Alterar médicos registrados e bloqueio de horários.</p>
          <a href="/settings/doctors" class="btn btn-primary">Acessar</a>
        </div>
      </div>
    </div>


  </div>
</main>