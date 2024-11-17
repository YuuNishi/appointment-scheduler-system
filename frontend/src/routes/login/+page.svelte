<script>
  import { onMount } from 'svelte';
  import 'iconify-icon';

  let email = '';
  let password = '';
  let token = null;

  async function handleSubmit(event) {
    event.preventDefault();

    const response = await fetch('http://localhost:8001/api/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    if (response.ok) {
      const data = await response.json();

      token = data.token;
      localStorage.setItem('token', token);
      window.location.href = '../appointments';
    } else {
      console.error('Erro de autenticação');
    }
  }

  onMount(() => {
    token = localStorage.getItem('token');
  });
</script>

<div class="login-container">
  <div class="login-left">
    <h1>Login como atendente</h1>
    <iconify-icon icon="emojione-v1:hospital" width="256" height="256"/>
  </div>

  <div class="login-right">
    <h2>Informe suas credenciais para acessar o sistema</h2>
    <form on:submit={handleSubmit}>
      <div class="mb-3">
        <label for="email" class="form-label">Endereço de email</label>
        <div class="input-icon">
          <iconify-icon icon="carbon:email" width="20" height="20"/>
          <input type="email" placeholder="usuario@dominio.com" class="form-control" id="email" bind:value={email} />
        </div>
      </div>

      <div class="mb-3">
        <label for="password" class="form-label">Senha</label>
        <div class="input-icon">
          <iconify-icon icon="mi:lock" width="20" height="20"/>
          <input type="password" class="form-control" id="password" bind:value={password} />
        </div>
      </div>

      <button type="submit" class="btn btn-login">LOGIN</button>
    </form>
    <a href="/password-recover">Esqueci minha senha</a>
  </div>
</div>

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

    @media(max-width: 800px) {
        .login-left {
            display: none;
        }
    }
</style>
