<script>
	import Sidebar from "../../components/sidebar/sidebar.svelte";
  
</script>

<main>
  <Sidebar />
  <div class="content">
    <h1>Novo Paciente</h1>
    <form method="POST" action="?/register" >
      <p>Geral</p>
      <div>
        <label for="name">Nome:</label>
        <input id="name"/>
      </div>
      <div>
        <label for="cpf">CPF:</label>
        <input type="text" id="cpf" placeholder=""/>
      </div>  
      <div>
        <label for="birthdate">Data Nascimento:</label>
        <input type="text" id="birthdate"/>
      </div>  
      <div>
        <label for="gender">Sexo:</label>
          <select id="gender">
              <option value="default">Selecione</option>
              <option value=0>Feminino</option>
              <option value=1>Masculino</option>
          </select> 
        
      </div> 
      
      
      <p>Endereço</p>
      <div>
        <label for="CEP">CEP:</label>
        <input id="CEP"/>  
      </div>  
      <div class="form-row">
          <div class="form-group col-md-6">
            <label for="street">Rua:</label>
            <input id="street"/>
          </div>  
          <div>
            <label for="number">Número:</label> 
            <input id="number"/>
          </div>  
      </div>
      <div>
        <label for="neighborhood">Bairro:</label>
        <input id="neighborhood"/>
      </div>
      <div>
        <label for="city">Cidade:</label>
        <input id="city"/>
      </div>  
      <div>
        <label for="state">Estado:</label>
        <input id="state"/>
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
  div {
    margin-bottom: 10px;
    margin-left: 2rem;
  }
  label {
    display: inline-block;
    width: 150px;
    text-align: right;;
  }
  #name{
    width: 65%;
  }
</style>
