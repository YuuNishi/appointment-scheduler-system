<script lang="ts">
  import 'iconify-icon';
  import { create_token } from '../../services/token.service.js';
  import type { CreateTokenType } from '../../types/services/token.types.js';
  import { goto } from '$app/navigation';
  import { setCookie } from '../../utils/cookies.utils';
  import ErrorToast from '../../components/toast/error_toast.svelte';
  import { userInformation } from '../../store/user.store';
  import LoadingSpinner from '../../components/spinner/loading_spinner.svelte';

  let isLoading: boolean;
  let showErrorToast: boolean;
  let toastError: string;

  let email = '';
  let password = '';

  async function handleSubmit(event: SubmitEvent) {
    event.preventDefault();

    const request: CreateTokenType = {
      email,
      password
    };

    try {
      isLoading = true;

      const response = await create_token(request);
      if (response.ok) {
        const { token, username } = await response.json();

        setCookie('token', token, 1);

        if (username) {
          $userInformation.username = username;
        }

        await goto('/appointments');
      }
      else if (response.status === 400 || response.status === 422) {
        showToast(0, 'Parâmetros inseridos são inválidos');
      }
      else if (response.status === 404) {
        showToast(0, 'Email e/ou senha de usuário inválidos');
      }
    } catch {
      showToast(0, 'Erro ao realizar autenticação');
    }
    finally {
      isLoading = false;
    }
  }

  function showToast(type: number, message: string) {
    if (type == 0) {
      toastError = message;
      showErrorToast = true;
    }
  }
</script>

<div class="login-container">

  {#if (isLoading)}
    <LoadingSpinner />
  {/if}

  <div class="login-left">
    <h1>Login como atendente</h1>
    <iconify-icon icon="emojione-v1:hospital" width="256" height="256" />
  </div>

  <div class="login-right">
    <h2>Informe suas credenciais para acessar o sistema</h2>
    <form on:submit={handleSubmit}>
      <div class="mb-3">
        <div>
          <label for="email" class="form-label">Endereço de email</label>
          <iconify-icon
            icon="material-symbols-light:help-outline"
            style="cursor: pointer;"
            data-toggle="tooltip"
            data-placement="top"
            title="Email deve ter até 100 caracteres"
          />
        </div>
        <div class="input-icon">
          <iconify-icon icon="carbon:email" width="20" height="20" />
          <input
            type="email"
            placeholder="usuario@dominio.com"
            class="form-control"
            id="email"
            maxlength="100"
            bind:value={email}
          />
        </div>
      </div>

      <div class="mb-3">
        <label for="password" class="form-label">Senha</label>
        <div class="input-icon">
          <iconify-icon icon="mi:lock" width="20" height="20" />
          <input type="password" class="form-control" id="password" bind:value={password} />
        </div>
      </div>

      <button type="submit" class="btn btn-login">LOGIN</button>
    </form>
  </div>
</div>

<ErrorToast bind:showErrorToast bind:toastError />

<style>
  .login-container {
    display: flex;
    height: 100vh;
    background-color: #f0f0f0;
  }

  .login-left {
    width: 50%;
    background-color: #e9e8f5;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    pointer-events: none;
  }

  .login-left h1 {
    font-size: 28px;
    margin-bottom: 20px;
    font-weight: bold;
    color: #000;
  }

  .login-right {
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px;
    background-color: #fff;
    max-width: 450px;
    margin: auto;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
  }

  .login-right h2 {
    margin-bottom: 20px;
    font-size: 18px;
    font-weight: bold;
    color: #000;
  }

  .form-label {
    font-size: 14px;
    font-weight: 500;
    color: #333;
  }

  .input-icon {
    display: flex;
    align-items: center;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
    margin-top: 5px;
  }

  .input-icon iconify-icon {
    margin-right: 8px;
    color: #666;
  }

  .form-control {
    border: none;
    outline: none;
    width: 100%;
    padding: 8px;
    font-size: 14px;
    color: #333;
  }

  .btn-login {
    width: 100%;
    padding: 10px;
    background-color: #0066ff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    margin-top: 20px;
  }

  .btn-login:hover {
    background-color: #0056d6;
  }

  a {
    display: block;
    text-align: center;
    margin-top: 10px;
    color: #0066ff;
    text-decoration: none;
    font-size: 14px;
  }

  a:hover {
    text-decoration: underline;
  }

  .mb-3 {
    margin-bottom: 16px;
  }

  .form-control:focus {
    outline: none;
    border-color: #0066ff;
  }

  @media (max-width: 800px) {
    .login-left {
      display: none;
    }
  }
</style>
