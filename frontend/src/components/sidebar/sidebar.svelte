<script lang="ts">
  import { page } from '$app/stores';
  import 'iconify-icon';
  import UserAvatar from '$lib/assets/placeholder_user.png';
  import { deleteCookie } from '../../utils/cookies.utils';
  import { isDarkTheme } from '../../store/theme.store';
  import { userInformation } from '../../store/user.store';

  let activePage = $page.url.pathname;
</script>

<div class="sidebar flex-column flex-shrink-0 p-3 {($isDarkTheme && 'text-white' && 'bg-dark') || ('bg-white')}">
  <div class="dropdown">
    <a
      class="d-flex align-items-center {$isDarkTheme && 'text-white'} text-decoration-none dropdown-toggle"
      id="dropdownUser"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      <img
        src={$userInformation.avatar}
        alt="user"
        width="32"
        height="32"
        class="rounded-circle me-2"
      />
      <strong>{$userInformation.username}</strong>
    </a>
    <ul class="dropdown dropdown-menu dropdown-menu-dark text-small shadow w-100 " aria-labelledby="dropdownUser">
      <li>
        <div class="dropdown-item form-check form-switch d-flex align-items-center justify-content-between px-3">
          <label class="form-check-label me-2" for="flexSwitchCheckChecked">
            Tema escuro
          </label>
          <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" bind:checked={$isDarkTheme} />
        </div>
      </li>
      <li><a class="dropdown-item" href="/settings">Configurações</a></li>
    </ul>
  </div>
  <hr />
  <ul class="nav nav-pills flex-column mb-auto gap-1">
    <li>
      <a href="/appointments" class="nav-link {(activePage == '/appointments' && 'active') || 'hover-link'} {$isDarkTheme && 'text-white'} d-flex align-items-center" aria-current="page">
        <iconify-icon icon="mdi:calendar-outline" width="28" height="28" class="me-2" />
        Agendamento
      </a>
    </li>
    <li>
      <a href="/records" class="nav-link {(activePage == '/records' && 'active') || 'hover-link' } {$isDarkTheme && 'text-white'} d-flex align-items-center">
        <iconify-icon icon="cuida:user-add-outline" width="28" height="28" class="me-2" />
        Prontuários
      </a>
    </li>
  </ul>
  <hr style="color: {($isDarkTheme && 'white') || 'black'}"/>
  <a on:click={() => {
    deleteCookie("token");
    deleteCookie("token_create");
  }} href="/login" class="nav-link {$isDarkTheme && 'text-white'} d-flex align-items-center">
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
