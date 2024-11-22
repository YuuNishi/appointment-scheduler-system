<script>
  import Sidebar from '../../components/sidebar/sidebar.svelte';
  //import Form from '../patients/-form.svelte';
  import Edit from '../edit/+page.svelte'
  import {onMount} from "svelte";
  import 'iconify-icon';

  //-----------------
  let showModal = false;
	let modalData;

  export let edit;

	function toggleModal(data) {
		modalData = data;
		showModal = !showModal;
	}
//----
function search() {

  var input, filter, table, tr, td,td2, i, txtValue,txtValue2;
  input = document.getElementById("inputdefault");
  filter = input.value.toUpperCase();
  table = document.getElementById("tb_patients");
  tr = table.getElementsByTagName("tr");

  //
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    td2= tr[i].getElementsByTagName("td")[1]
    if (td) {
      txtValue = td.textContent || td.innerText;
      txtValue2 = td2.textContent || td2.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1 || txtValue2.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
///
let isSorted = false
function sortTable(patients) {
  if(!isSorted){
    patients.sort((a, b) => a.name.localeCompare(b.name))
    location.replace(location.href)
  }else{
    patients.sort((a, b) => b.name.localeCompare(a.name))
    isSorted= false
    
  }
}

///


  export let data
  
  const {patients} = data

  
  let chunks = [];

// Loop to split array into chunks
  for (let i = 0; i < patients.length; i += 10) {
    let chunk = [];
    
    // Iterate for the size of chunk
    for (let j = i; j < i + 10 && j < patients.length; j++) {
        chunk.push(patients[j]);
    }
    
    // push the chunk to output array
    chunks.push(chunk);
}
</script>

<main>
  <Sidebar />
  <div class="content">
    <h1>Prontuários</h1>
    <div class="form-group">
      <input class="form-control" id="inputdefault" type="text" placeholder="Digite o nome ou CPF" on:keyup={search}>
    </div>

    <div>
      
    </div>

    <div class="results">
      <div class="text-right">
        <button class="btn " >
          <iconify-icon on:click={sortTable()} icon="bi:filter" width="1.8em" height="1.8em" class="icon"></iconify-icon>
        </button>
        <a href="/register">
          <button class="btn btn-success">Novo Paciente</button>
        </a>
      </div>

      <table class="table" id="tb_patients">
        <thead>
          <tr>
            <th scope="col">Nome</th>
            <th scope="col">CPF</th>
            <th scope="col">Sexo</th>
            <th scope="col">Data de nascimento</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {#each patients as person}
            <tr>
              <td>{person.name}</td>
              <td>{person.cpf}</td>
              {#if person.sex ==1}
                <td>Feminino</td>
              {:else}
                <td>Masculino</td>
              {/if}
              <td>{person.birth_date.split("-").reverse().join("-")}</td>
              <td>
                  <iconify-icon  icon="subway:pencil" width="1.2em" on:click={()=>(toggleModal({person}))} height="1.2em" class="icon icon-edit"></iconify-icon>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
      {#if showModal}
	      
        <Edit on:click={toggleModal} {edit} bind:values={modalData}/>
        
      {/if}
    </div>
    
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
  .btn{
    float: right;
    margin: 1%;
  }
  .icon{
    color: rgb(61, 152, 255);
  }
  .results{
    margin-top: 1rem;
    background-color: #FFFFFF;
    padding-top: 2rem;
  }
  .icon-edit{
    align-self: right;
    cursor: pointer;
  }
</style>
