<script lang="ts">
  import LoadingSpinner from '../../components/spinner/loading_spinner.svelte';
  import Sidebar from '../../components/sidebar/sidebar.svelte';
  import { isDarkTheme } from '../../store/theme.store';
  import Breadcrumb from '../../components/breadcrumb/breadcrumb.svelte';
  import type { BreadCrumbItemType } from '../../types/services/shared.types';

  let isLoading: boolean;

  let breadCrumbItems: BreadCrumbItemType[] = [
    {
      route: "settings",
      title: "configurações",
      active: true
    }
  ]
</script>

<main>
  <Sidebar />

  {#if (isLoading)}
    <LoadingSpinner />
  {/if}

  <div class="content {$isDarkTheme && 'text-white'} {($isDarkTheme && 'content-background-dark') || 'content-background-white'}">
    <Breadcrumb breadCrumbItems={breadCrumbItems} />

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