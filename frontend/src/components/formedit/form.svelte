<script>
    import { imask } from '@imask/svelte';
	export let modalData;
    const options = { 
    date: '00/00/0000',
    cpf: '000.000.000-00'
	};
    let patient = JSON.stringify(modalData.person)
    patient = JSON.parse(patient)

    let updatePatient = pd =>{
        newPatient = {
            "name": "Nayuta",
            "status": 2,
            "sex": 1,
            "birth_date": "2004-11-19",
            "cpf": "111.111.111",
            "address_id": 2
        }
        
    }
</script>

<div on:click|self class='modal'>
	<div class='content'>

        <h1>Editar Paciente</h1>
        <form method="POST">
            <div class="row g-2 align-items-center">
                <div class="col-auto">
                <label for="name">Nome:</label>
                </div>
                <div class="col-md-6">
                <input id="name" name="name" required value={patient["name"]} class="form-control"/>
                </div>
            </div>
            
            <div class="row g-2 align-items-center">
                <div class="col-auto">
                <label for="cpf">CPF:</label>
                </div>
                <div class="col-md-4">
                <input use:imask={options.cpf} name="cpf" value={patient["cpf"]} class="form-control" type="text" id="cpf" placeholder="___.___.___-__"/>
                </div>
            </div>

            <div class="row g-2 align-items-center">
                <div class="col-auto">
                <label for="birthdate">Data Nascimento:</label>
                </div>
                <div class="col-md-4">
                <input use:imask={options.date} class="form-control" value={patient["birth_date"].split("-").reverse().join("/")} type="text" name="birthdate" id="birthdate" placeholder="__/__/____"/>
                </div>
            </div>

            <div class="row g-2 align-items-center">
                <div class="col-auto">
                <label for="gender">Sexo:</label>
                </div>
                <div class="col-md-2">
                <select id="gender" name="gender" class="form-control">
                    {#if patient["sex"]==0}
                        <option value=0 selected>Masculino</option>
                        <option value=1>Feminino</option>
                    {:else}
                        <option value=0>Masculino</option>
                        <option value=1 selected>Feminino</option>
                    {/if}
                </select> 
                </div>
            </div>
            <button on:click class="btn btn-default">Cancelar</button>
            <button on:click class="btn btn-success" type="submit">Salvar</button>
        </form>
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
    .btn-default{
        border-color: black;
    }
    .btn-default:hover {
        background-color:#dfdede;
        transition: 0.7s;
    }
</style>