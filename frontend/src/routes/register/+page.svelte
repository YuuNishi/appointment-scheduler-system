<script lang="ts">
	import Sidebar from "../../components/sidebar/sidebar.svelte";
  import { imask } from '@imask/svelte';
  
  const options = { 
    date: '00/00/0000',
    cpf: '000.000.000-00',
    cep: '00000-000'
	};
  const estates= [{nome:'Acre', sigla:'AC'},
{nome:'Alagoas', sigla:'AL'},
{nome:'Amapá', sigla:'AP'},
{nome:'Amazonas', sigla:'AM'},
{nome:'Bahia', sigla:'BA'},
{nome:'Ceará', sigla:'CE'},
{nome:'Espírito Santo', sigla:'ES'},
{nome:'Goiás', sigla:'GO'},
{nome:'Maranhão', sigla:'MA'},
{nome:'Mato Grosso', sigla:'MT'},
{nome:'Mato Grosso do Sul', sigla:'MS'},
{nome:'Minas Gerais', sigla:'MG'},
{nome:'Pará', sigla:'PA'},
{nome:'Paraíba', sigla:'PB'},
{nome:'Paraná', sigla:'PR'},
{nome:'Pernambuco', sigla:'PE'},
{nome:'Piauí', sigla:'PI'},
{nome:'Rio de Janeiro', sigla:'RJ'},
{nome:'Rio Grande do Norte', sigla:'RN'},
{nome:'Rio Grande do Sul', sigla:'RS'},
{nome:'Rondônia', sigla:'RO'},
{nome:'Roraima', sigla:'RR'},
{nome:'Santa Catarina', sigla:'SC'},
{nome:'São Paulo', sigla:'SP'},
{nome:'Sergipe', sigla:'SE'},
{nome:'Tocantins', sigla:'TO'},
{nome:'Distrito Federal', sigla:'DF'}
]


</script>

<main>
  <Sidebar />
  <div class="content">
    <h1>Novo Paciente</h1>
    <form method="POST" action="?/create">
      <p>Geral</p>
      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="name">Nome:</label>
        </div>
        <div class="col-md-6">
          <input id="name" name="name" required class="form-control"/>
        </div>
      </div>
      
      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="cpf">CPF:</label>
        </div>
        <div class="col-md-2">
          <input use:imask={options.cpf} name="cpf" required class="form-control" type="text" id="cpf" placeholder="___.___.___-__"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="birthdate">Data Nascimento:</label>
        </div>
        <div class="col-md-2">
          <input use:imask={options.date} class="form-control" required type="text" name="birthdate" id="birthdate" placeholder="__/__/____"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="gender">Sexo:</label>
        </div>
        <div class="col-md-2">
          <select id="gender" name="gender" required class="form-control">
            <option value="" selected disabled hidden >Selecione</option>
            <option value=0>Masculino</option>
            <option value=1>Feminino</option>
          </select> 
        </div>
      </div>
      <p>Endereço</p>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="cep">CEP:</label>
        </div>
        <div class="col-md-2">
          <input use:imask={options.cep} id="cep" name="cep" required class="form-control" placeholder="_____-__"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="street">Rua:</label>
        </div>
        <div class="col-md-6">
          <input id="street" name="street" required class="form-control"/>
        </div>
        <div class="col-auto">
          <label for="number">Número:</label> 
        </div>
        <div class="col-md-2 ">
          <input id="number" type="number" required name="number" class="form-control"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="neighborhood">Bairro:</label> 
        </div>
        <div class="col-md-6">
          <input id="neighborhood" name="neighborhood" required type="text" class="form-control"/>
        </div>
      </div>

      <div class="row g-2 align-items-center">
        <div class="col-auto">
          <label for="city">Cidade:</label>
        </div>
        <div class="col-md-4">
          <input id="city" name="city" type="text" required class="form-control"/>
        </div>
        <div class="col-auto">
          <label for="state">Estado:</label>
        </div>
        <div class="col-md-auto">
          <select id="state" name="state" required class="form-control">
            <option value="" selected disabled hidden >Selecione</option>
            {#each estates as estate}
              <option value={estate.sigla}>{estate.nome}</option>
            {/each}
          </select> 
        </div>
      </div>

      <div class="row">
        <div class="col align-self-end">
          <a href="/patients">
            <button type="button" class="btn btn-default btn-outline" >Voltar sem salvar</button>
          </a>
          <button class="btn btn-success" type="submit">Salvar</button>
        </div>
      </div>
      
      
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
  .btn-default{
    border-color: black;
  }
  .btn-default:hover {
    background-color:#dfdede;
    transition: 0.7s;
  }
</style>
