<script lang="ts">
    import { onMount } from 'svelte';
    import Sidebar from '../../components/sidebar/sidebar.svelte';
    import type { GetAllPatientType } from '../../types/services/patient.types';
    import { get_all_patients, remove_patient } from '../../services/patient.service';
    import LoadingSpinner from '../../components/spinner/loading_spinner.svelte';
    import { isDarkTheme } from '../../store/theme.store';
    import type { BreadCrumbItemType } from '../../types/services/shared.types';
    import Edit from '../edit/+page.svelte'
    let patients: GetAllPatientType[] = [];

  export let showModal = false;
	let modalData;

  export let edit;
  export let form
	function toggleModal(data) {
		modalData = data;
		showModal = !showModal;
	}

    onMount(()=>{
        getAllPatients()
    })

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

    async function getAllPatients() {
    patients = [];

    let result = await get_all_patients();

    patients = await result.json();
    patients.reverse()
  }

let isSorted = false
function sortTable() {
  if(!isSorted){
    patients = patients.sort((a, b) => a.name.localeCompare(b.name))
    isSorted = true
  }else{
    patients=patients.sort((a, b) => b.name.localeCompare(a.name))
    isSorted= false
  }
}
function onClickDelete(id:number){
    deletePatient(id)
}

async function deletePatient(id: number){
    await remove_patient(id)
}
  </script>
    
  <main>
    <Sidebar />
  
    <div class="content {($isDarkTheme && 'content-background-dark') || 'content-background-white'}">
        <h1>Prontuários</h1>

        <div class="form-group">
            <input class="form-control" id="inputdefault" type="text" placeholder="Digite o nome ou CPF" on:keyup={search}>
        </div>

        <div class="results">
            <div class="text-right">
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
                {#each patients as person}
                  <tr>
                    <td>{person.name}</td>
                    <td>{person.cpf}</td>
                    {#if person.sex ==1}
                      <td>Feminino</td>
                    {:else}
                      <td>Masculino</td>
                    {/if}
                    <td>{person.birth_date}</td>
                    <td>
                        <iconify-icon  icon="subway:pencil" width="1.2em" on:click={()=>(toggleModal({person}))} height="1.2em" class="icon icon-edit"></iconify-icon>
                    </td>
                    <td>
                        <button type="submit" class="btn btn-default" on:click={()=>{onClickDelete(person.id)}}>
                          <iconify-icon  icon="material-symbols:delete" width="1.2em" height="1.2em" class="icon icon-edit"></iconify-icon>
                        </button>
                    </td>
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>
          {#if showModal}
	      
            <Edit on:click={toggleModal} {edit} {form} bind:values={modalData} bind:show={showModal} />
          {/if}
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
