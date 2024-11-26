<script>
    import { imask } from "@imask/svelte";
    import {enhance} from '$app/forms'
    export let edit, values, show
    export let form
    export let pat = JSON.stringify(values.person)
    pat = JSON.parse(pat)
    const options = { 
    date: '00/00/0000',
    cpf: '000.000.000-00'
	};

</script>
<div>
    <div on:click|self class='modal'>
        <div class='content'>
            <h1>Editar paciente</h1>
            <form method="post" action="/patients?/updatePatient" use:enhance={()=>{ 
                return async({update, result})=>{
                    if(result.type ==='success'){
                        show = false
                    }else{
                        update({reset: false})
                    }  
                    }}}>

            <input name="id" id="id" type="text" hidden value={pat["id"]}>

            <div class="row g-2 align-items-center">
                <div class="col-auto">
                    <label for="name">Nome:</label>
                </div>
                <div class="col-md-6">
                    <input id="name" name="name" required value={pat["name"]} class="form-control"/>
                </div>
            </div>
            <div class="row g-2 align-items-center">
                <div class="col-auto">
                    <label for="cpf">CPF:</label>
                </div>
                <div class="col-md-6">
                    <input use:imask={options.cpf} id="cpf" name="cpf" minlength="14" required value={pat["cpf"]} class="form-control"/>
                </div>
            </div>
            <div class="row g-2 align-items-center">
                <div class="col-auto">
                    <label for="birthdate">Data de Nascimento:</label>
                </div>
                <div class="col-md-6">
                    <input use:imask={options.date} id="birthdate" name="birthdate" minlength="10" required value={pat["birth_date"].split("-").reverse().join("/")} class="form-control"/>
                    {#if form?.invalid}
                        <p class="error" >Data inválida</p>
                    {/if}
                </div>
            </div>
            <div class="row g-2 align-items-center">
                <div class="col-auto">
                <label for="gender">Sexo:</label>
                </div>
                <div class="col-md-2">
                <select id="gender" name="gender" class="form-control">
                    {#if pat["sex"]==0}
                        <option value=0 selected>Masculino</option>
                        <option value=1>Feminino</option>
                    {:else}
                        <option value=0>Masculino</option>
                        <option value=1 selected>Feminino</option>
                    {/if}
                </select> 
                </div>
            </div>

            <div class="row g-2 align-items-center">
                <div class="col-auto">
                <label for="status">Status:</label>
                </div>
                <div class="col-md-2">
                <select id="status" name="status" class="form-control">
                    {#if pat["status"]==0}
                        <option value=0 selected>Inativo</option>
                        <option value=1>Ativo</option>
                    {:else}
                        <option value=0>Inativo</option>
                        <option value=1 selected>Ativo</option>
                    {/if}
                </select> 
                </div>
            </div>
                <a href="/patients">
                    <button on:click class="btn btn-outline-danger">Cancelar</button>
                </a>
                    <button type="submit" class="btn btn-success" >Edit</button>     
            </form> 
        </div>
    </div>
</div>
<style>
	.modal {
		background-color: rgba(0, 0, 0, 0.4);
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	
	.content {
		background-color: white;
        border-radius: 12px;
        padding: 20px;
		width: 50%;
		height: 80%;
	}
    form{
    background-color: white;
    padding: 1rem;
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
    .error{
        color: red;
    }
</style>