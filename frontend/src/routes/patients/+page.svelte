<script>
  import Sidebar from '../../components/sidebar/sidebar.svelte';
  import Edit from '../edit/+page.svelte'
  import 'iconify-icon';

  //-----------------
  export let showModal = false;
	let modalData;

  export let edit;
  export let form
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


  export let data
  
  const {patients} = data

  
  let chunks = [];
  for (let i = 0; i < patients.length; i += 6) {
    let chunk = [];
    for (let j = i; j < i + 6 && j < patients.length; j++) {
        chunk.push(patients[j]);
    }
    chunks.push(chunk);
  }
  let patientPage = chunks[0]
  function pagination(n){
      patientPage= chunks[n]
    
  }
  let isSorted = false
function sortTable() {
  if(!isSorted){
    patientPage = patientPage.sort((a, b) => a.name.localeCompare(b.name))
    isSorted = true
  }else{
    patientPage=patientPage.sort((a, b) => b.name.localeCompare(a.name))
    isSorted= false
  }
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
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            {#each chunks as c, i}
              <li class="page-item"><button class="page-link" on:click={()=>pagination(i)} >{i+1}</button></li>
            {/each}
          </ul>
        </nav>
        <button class="btn control" on:click={()=>sortTable()} >
          <iconify-icon  icon="bi:filter" width="1.8em" height="1.8em" class="icon"></iconify-icon>
        </button>
        <a href="/register">
          <button class="btn btn-success control">Novo Paciente</button>
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
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {#each patientPage as person}
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
              <td>
                <form method="post" action="?/deletePatient">
                  <button type="submit" class="btn btn-default">
                    <input type="text" id="id" name="id" hidden value={person.id}>
                    <iconify-icon  icon="material-symbols:delete" width="1.2em" height="1.2em" class="icon icon-edit"></iconify-icon>
                  </button>
                </form>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
      {#if showModal}
	      
        <Edit on:click={toggleModal} {edit} {form} bind:values={modalData} bind:show={showModal} />
        
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
  .control{
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
