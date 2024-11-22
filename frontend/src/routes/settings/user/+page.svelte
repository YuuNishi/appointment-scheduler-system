<script lang="ts">
  import LoadingSpinner from '../../../components/spinner/loading_spinner.svelte';
  import Sidebar from '../../../components/sidebar/sidebar.svelte';
  import { isDarkTheme } from '../../../store/theme.store';
  import { userInformation } from '../../../store/user.store';
  import type { PageData } from './$types';
  import type { UserInfoResponseType } from '../../../types/services/user.types';

  let data: PageData;
  let getUserInfo: UserInfoResponseType = data.userInfo;

  let isLoading: boolean;
  let selectedAvatar: string;
  let username: string = getUserInfo.username;
  let currentPassword: string = '';
  let newPassword: string = '';
  let showAvatarOptions: boolean = false;

  async function updateUsername() {

  }

  async function updatePassword() {

  }

  function toggleAvatarOptions() {
    showAvatarOptions = !showAvatarOptions;
  }

  function selectAvatar(avatar: string) {
    selectedAvatar = avatar;
    showAvatarOptions = false;
  }
</script>

<main>
  <Sidebar />

  {#if (isLoading)}
    <LoadingSpinner />
  {/if}

  <div class="content {($isDarkTheme && 'content-background-dark') || 'content-background-white'}">
    <h1>Configurações do Usuário</h1>

    <section class="mb-4">
      <h2>Avatar</h2>
      <div class="avatar-wrapper">
        <img
          src={$userInformation.avatar}
          alt="Avatar atual"
          class="rounded-circle me-3"
          style="width: 80px; height: 80px; cursor: pointer;"
          on:click={toggleAvatarOptions}
        />
        <div class="avatar-overlay">
          <span>Alterar Avatar</span>
        </div>
      </div>

      {#if showAvatarOptions}
        <div class="mt-3">
          <h5>Selecione um avatar:</h5>
          <div class="avatar-grid d-flex gap-3">
            {#each ['avatar1.png', 'avatar2.png', 'avatar3.png'] as avatar}
              <img
                src={$userInformation.avatar}
                alt="avatar"
                class="rounded-circle border"
                style="width: 50px; height: 50px; cursor: pointer; border-width: {selectedAvatar === avatar ? '3px' : '1px'};"
              />
            {/each}
          </div>
        </div>
      {/if}
    </section>

    <section class="mb-4">
      <div class="form-group">
        <label for="usernameInput">Nome de Usuário</label>
        <input type="text" class="form-control" id="usernameInput" bind:value={username} placeholder="Novo nome de usuário" />
      </div>
    </section>

    <section class="mb-4">
      <div class="form-group">
        <label for="currentPassword">Senha Atual</label>
        <input type="password" class="form-control" id="currentPassword" bind:value={currentPassword} placeholder="Senha atual" />
      </div>
      <div class="form-group">
        <label for="newPassword">Nova Senha</label>
        <input type="password" class="form-control" id="newPassword" bind:value={newPassword} placeholder="Nova senha" />
      </div>
      <button class="btn btn-primary mt-2" on:click={updatePassword}>Atualizar Senha</button>
    </section>
  </div>
</main>

<style>
    .avatar-wrapper {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }

    .avatar-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* Fundo semi-transparente */
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: opacity 0.3s ease;
        border-radius: 50%; /* Mantém o formato redondo */
    }
</style>