<script lang="ts">
  import LoadingSpinner from '../../../components/spinner/loading_spinner.svelte';
  import Sidebar from '../../../components/sidebar/sidebar.svelte';
  import { isDarkTheme } from '../../../store/theme.store';
  import { userInformation } from '../../../store/user.store';
  import { update_avatar, update_password, update_username } from '../../../services/user.service';
  import ErrorToast from '../../../components/toast/error_toast.svelte';
  import SuccessToast from '../../../components/toast/success_toast.svelte';
  import Breadcrumb from '../../../components/breadcrumb/breadcrumb.svelte';
  import type { BreadCrumbItemType } from '../../../types/services/shared.types';
  import { get_avatar_by_enum } from '../../../utils/avatar.utils';
  import { UserAvatarEnum } from '../../../enums/store.enums';

  export let data;

  resetUserInformation(data.userInfo.username);

  let showErrorToast: boolean;
  let toastError: string;
  
  let showSuccessToast: boolean;
  let toastSuccess: string;  

  let breadCrumbItems: BreadCrumbItemType[] = [
    {
      route: "/settings",
      title: "configurações",
      active: false
    },
    {
      route: "/settings/user",
      title: "usuário",
      active: true
    }
  ]

  const avatars: UserAvatarEnum[] = [
    UserAvatarEnum.placeholder,
    UserAvatarEnum.assistant,
    UserAvatarEnum.female_doc,
    UserAvatarEnum.male_doc
  ];

  let isLoading: boolean;
  let selectedAvatar: UserAvatarEnum | null = null;
  let username: string = $userInformation.username;
  let currentPassword: string = '';
  let newPassword: string = '';
  let showAvatarOptions: boolean = false;

  async function addNewPassword(){
    isLoading = true;
    if (currentPassword && newPassword && currentPassword != newPassword) {
      await updatePassword();
    }else if(currentPassword === newPassword && currentPassword != "" && newPassword != ""){
      showToast(0, "Nova Senha é Igual a Senha Atual");
    }else if(currentPassword === "" && newPassword === ""){
      showToast(0, "Você deve Preencher os campos para redefinir a senha");
    }else if(currentPassword === ""){
      showToast(0, "Campo da senha atual está vazio");
    }else if(newPassword === ""){
      showToast(0, "Campo da nova senha está vazio");
    }
    isLoading = false;    
  }

  async function addNewAvatar(){
    isLoading = true;
    if (selectedAvatar != null && $userInformation.avatar !== get_avatar_by_enum(selectedAvatar)) {
      await updateAvatar();
    }else if($userInformation.avatar === get_avatar_by_enum(selectedAvatar)){
      showToast(0, "Voce deve escolher um avatar para alterar");
    }
    isLoading = false;
  }

  async function addNewUsername() {
    isLoading = true;

    username = username.trim();

    if (username && username != $userInformation.username) {
      await updateUsername();
    }else if(username === $userInformation.username){
      showToast(0, "Novo nome de usuário é igual ao nome anterior ");
    }else if(username === ""){
      showToast(0, "Campo nome de usuário está vazio");
    }

    isLoading = false;
  }

  function resetUserInformation(username: string) {
    $userInformation.username = username;
  }

  async function updateUsername() {
    let data = await update_username({ username })

    if (data.ok) {
      let dataJson = await data.json();
      resetUserInformation(dataJson.username);
      showToastSuccess(1, "Nome Atualizado com Sucesso");
    }
    else if (data.status === 409) {
      showToast(0, "Nome de usuário já está sendo utilizado no momento");
    }
    else if(username.length < 10){
      showToast(0, "O nome do usuário deve ter mais de 10 caracteres");
    }else {
      showToast(0, "Ocorreu um erro ao atualizar nome de usuário");
    }
  }

  async function updatePassword() {
    let data = await update_password({ oldPassword: currentPassword, newPassword});

    if (data.ok) {
      let dataJson = await data.json();
      username = dataJson.username;
      showToastSuccess(1, "Senha atualizada com sucesso");
      
        setTimeout(() => {
            currentPassword = '';
            newPassword = "";
        }, 0);
    }
    else if (data.status === 404) {
      showToast(0, "Senha atual incorreta");
    }
  }

  async function updateAvatar() {
    let data = await update_avatar({ avatar: selectedAvatar! });

    if (data.ok) {
      $userInformation.avatar = get_avatar_by_enum(selectedAvatar!);
      showToastSuccess(1, "Avatar atualizado com sucesso");
    }
    else {
      showToast(0, "Erro inesperado ao alterar o avatar");
    }
  }

  function toggleAvatarOptions() {
    showAvatarOptions = !showAvatarOptions;
  }

  function selectAvatar(avatar: UserAvatarEnum) {
    selectedAvatar = avatar;
    showAvatarOptions = false;
  }

  function showToast(type: number, message: string) {
    if (type == 0) {
      toastError = message;
      showErrorToast = true;
    }
  }

  function showToastSuccess(type: number, message: string) {
    if (type == 1) {
      toastSuccess = message;
      showSuccessToast = true;
    }
    function clearInput(idInput: string){
      document.getElementById(idInput).value = "";
    }
  }

</script>

<main>
  <Sidebar />

  {#if isLoading}
    <LoadingSpinner />
  {/if}

  <div class="content {($isDarkTheme && 'content-background-dark') || 'content-background-white'}">
    <Breadcrumb breadCrumbItems={breadCrumbItems} />

    <h1>Configurações de Usuário</h1>

    <section class="mb-4">
      <div class="avatar-wrapper me-3">
        <img
          src={selectedAvatar !== null ? get_avatar_by_enum(selectedAvatar) : $userInformation.avatar}
          alt="Avatar atual"
          class="rounded-circle"
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
          <div class="d-flex gap-3">
            {#each avatars as avatar}
              <div on:click={() => selectAvatar(avatar)}>
                <img
                  src={get_avatar_by_enum(avatar)}
                  alt="avatar"
                  class="rounded-circle avatar-item border"
                  style="border-width: {selectedAvatar === avatar
                  ? '3px'
                  : '1px'};"
                />
              </div>
            {/each}
          </div>
        </div>
      {/if}
    </section>

    <button class="btn btn-primary mb-4" on:click={addNewAvatar}>Alterar Avatar</button>

    <section class="mb-4">
      <div class="form-group">
        <label for="usernameInput">Nome de Usuário</label>
        <input
          type="text"
          class="form-control"
          id="usernameInput"
          bind:value={username}
          placeholder="Novo nome de usuário"
        />
      </div>
    </section>
    
    <button class="btn btn-primary mb-4" on:click={addNewUsername}>Atualizar Nome</button>

    <section class="mb-4">
      <div class="form-group">
        <label for="currentPassword">Senha Atual</label>
        <input
          type="password"
          class="form-control"
          id="currentPassword"
          bind:value={currentPassword}
          placeholder="Senha atual"
        />
      </div>
      <div class="form-group">
        <label for="newPassword">Nova Senha</label>
        <input
          type="password"
          class="form-control"
          id="newPassword"
          bind:value={newPassword}
          placeholder="Nova senha"
        />
      </div>
    </section>
    <button class="btn btn-primary mt-2" on:click={addNewPassword}>Atualizar Senha</button>
  </div>
</main>

<ErrorToast bind:showErrorToast bind:toastError />
<SuccessToast bind:showSuccessToast bind:toastSuccess />

<style>
  .avatar-wrapper {
    position: relative;
    display: inline-block;
    cursor: pointer;
  }

  .avatar-overlay {
    bottom: 0;
    width: 100%;
    height: 100%;
    display: flex;
  }

  .avatar-item {
      width: 50px;
      height: 50px;
      cursor: pointer;
  }
</style>
