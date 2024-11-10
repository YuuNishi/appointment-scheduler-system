<script>
  import { onMount } from 'svelte';

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
      body: JSON.stringify({   
 email, password })
    });

    if (response.ok) {
      const data = await response.json();   

      token = data.token;

      console.log(token)

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


<div class="bg-secondary d-flex align-items-center justify-content-center" style="height: 100vh;">
  <div class="row">
    <div class="col-md-6">
      <div class="card">
        <div class="card-body bg-primary">
          <h5 class="card-title">Login como Atendente</h5>
          <img src="hospital.png" alt="Hospital Image" class="img-fluid mb-3">
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Informe suas credenciais para acessar o sistema</h5>
          <form on:submit={handleSubmit}>
            <div class="mb-3">
              <label for="email" class="form-label">Endereço de Email</label>
              <input type="email" placeholder="user@service.com" class="form-control" id="email" bind:value={email}>   

            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Senha</label>
              <input type="password" class="form-control" id="password" bind:value={password}>   

            </div>
            <button type="submit" class="btn btn-primary">Entrar</button>
          </form>
        </div>
      </div>
    </div>
  </div>   
</div>