<script>
	import Sidebar from "../../components/sidebar/sidebar.svelte";
  import { imask } from '@imask/svelte';
  
  const options = { 
    date: '00/00/0000',
    cpf: '000.000.000-00',
    cep: '00000-000'
	};

</script>

<main>
  <Sidebar />
  <div class="content">
    <h1>Novo Paciente</h1>
    <form method="POST" action="?/register" >
      <p>Geral</p>
      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="name">Nome:</label>
        </div>
        <div class="col-md-6">
          <input id="name" class="form-control"/>
        </div>
      </div>
      
      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="cpf">CPF:</label>
        </div>
        <div class="col-md-2">
          <input use:imask={options.cpf} class="form-control" type="text" id="cpf" placeholder="___.___.___-__"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="birthdate">Data Nascimento:</label>
        </div>
        <div class="col-md-2">
          <input use:imask={options.date} class="form-control" type="text" id="birthdate" placeholder="__/__/____"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="gender">Sexo:</label>
        </div>
        <div class="col-md-2">
          <select id="gender" class="form-control">
            <option value="default">Selecione</option>
            <option value=0>Feminino</option>
            <option value=1>Masculino</option>
          </select> 
        </div>
      </div>
      <p>Endereço</p>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="CEP">CEP:</label>
        </div>
        <div class="col-md-2">
          <input use:imask={options.cep} id="CEP" class="form-control" placeholder="_____-__"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="street">Rua:</label>
        </div>
        <div class="col-md-6">
          <input id="street" class="form-control"/>
        </div>
        <div class="col-auto">
          <label for="number">Número:</label> 
        </div>
        <div class="col-md-2 ">
          <input id="number" type="number" class="form-control"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="neighborhood">Bairro:</label> 
        </div>
        <div class="col-md-6">
          <input id="neighborhood" type="text" class="form-control"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="city">Cidade:</label>
        </div>
        <div class="col-md-4">
          <input id="city" type="text" class="form-control"/>
        </div>
        <div class="col-auto">
          <label for="state">Estado:</label>
        </div>
        <div class="col-md-auto">
          <select id="state" class="form-control">
            <option value="default">Selecione</option>
            <option value=0>Feminino</option>
            <option value=1>Masculino</option>
          </select> 
        </div>
      </div>

      <button type="button" class="btn btn-default btn-outline" >Voltar sem salvar</button>
      <button class="btn btn-success">salvar</button>
    </form>  
  </div>
</main>

<style>
  main {
    display: flex;
  }
  .content {
    flex: 1;
    background-color: #F0F0F0;
    padding: 20px;
  }
  form{
    background-color: white;
    padding: 2rem;
  }
  p{
    color: #5398ec;
  }
  div.row {
    margin-bottom: 10px;
    margin-left: 2rem;
  }
  
  label {
    display: inline-block;
    width: 150px;
    text-align: right;;
  }
</style>
