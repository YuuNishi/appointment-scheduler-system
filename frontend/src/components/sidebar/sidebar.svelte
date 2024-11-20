<script lang="ts">
  import { onMount } from 'svelte'
  import { page } from '$app/stores';
  import 'iconify-icon';
  import UserAvatar from '$lib/assets/placeholder_user.png';
  import { deleteCookie } from '../../utils/cookies.utils';

  let activePage = $page.url.pathname;
  let isDarkMode : boolean;

  export { isDarkMode }

  onMount(() => (isDarkMode = false));
</script>

<div class="sidebar flex-column flex-shrink-0 p-3 {(isDarkMode && 'text-white' && 'bg-dark') || ('bg-white')}">
  <div class="dropdown">
    <a
      class="d-flex align-items-center {isDarkMode && 'text-white'} text-decoration-none dropdown-toggle"
      id="dropdownUser"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      <img
        src={UserAvatar}
        alt="user"
        width="32"
        height="32"
        class="rounded-circle me-2"
      />
      <strong>Usuário</strong>
    </a>
    <ul class="dropdown dropdown-menu dropdown-menu-dark text-small shadow w-100 " aria-labelledby="dropdownUser">
      <li>
        <div class="dropdown-item form-check form-switch d-flex align-items-center justify-content-between px-3">
          <label class="form-check-label me-2" for="flexSwitchCheckChecked">
            Tema escuro
          </label>
          <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" bind:checked={isDarkMode} />
        </div>
      </li>
      <li><a class="dropdown-item" href="/settings">Configurações</a></li>
    </ul>
  </div>
  <hr />
  <ul class="nav nav-pills flex-column mb-auto gap-1">
    <li>
      <a href="/appointments" class="nav-link {(activePage == '/appointments' && 'active') || 'hover-link'} {isDarkMode && 'text-white'} d-flex align-items-center" aria-current="page">
        <iconify-icon icon="mdi:calendar-outline" width="28" height="28" class="me-2" />
        Agendamento
      </a>
    </li>
    <li>
      <a href="/records" class="nav-link {(activePage == '/records' && 'active') || 'hover-link' } {isDarkMode && 'text-white'} d-flex align-items-center">
        <iconify-icon icon="cuida:user-add-outline" width="28" height="28" class="me-2" />
        Prontuários
      </a>
    </li>
  </ul>
  <hr style="color: {(isDarkMode && 'white') || 'black'}"/>
  <a on:click={() => {
    deleteCookie("token");
    deleteCookie("token_create");
  }} href="/login" class="nav-link {isDarkMode && 'text-white'} d-flex align-items-center">
    <iconify-icon icon="dashicons:exit" width="28" height="28" class="me-2" />
    Sair
  </a>
</div>

<style>
  .sidebar {
    width: 260px;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    overflow-y: auto;
  }

  .hover-link:hover {
    background-color: #72727242;
  }

  a {
    cursor: pointer;
  }
</style>
