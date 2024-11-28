<script lang="ts">
  import { update_patient } from '../../services/patient.service';
  import type { UpdatePatientType } from '../../types/services/patient.types';
  import { imask } from '@imask/svelte';

  export let values, show;
  export let pat = JSON.stringify(values.person);
  pat = JSON.parse(pat);

  const options = {
    cpf: '000.000.000-00'
  };

  const gen = [
    { text: 'Feminino', value: 1 },
    { text: 'Maculino', value: 0 }
  ];

  const stat = [
    { text: 'Ativo', value: 1 },
    { text: 'Inativo', value: 0 }
  ];
  
  let validDate = true;
  function dateIsValid() {
    if (isNaN(new Date(formDate.split('/').reverse().join('/') + '/')) || formDate.length < 10) {
      validDate = false;
    } else {
      validDate = true;
    }
  }
  async function onClickUpdate()
  {
    const cpf = pat['cpf'].replaceAll('.', '').replace('-', '');

    const patientData: UpdatePatientType = {
      name: pat['name'],
      status: pat['status'],
      sex: pat['sex'],
      birth_date: pat['birth_date'],
      cpf,
      address_id: 0
    };
    try {
      await update_patient(patientData, pat['id']);
      show = false;
    } catch {
      return;
    }
  }
</script>

<div>
  <div on:click|self class="modal">
    <div class="content">
      <h1>Editar paciente</h1>
      <form>
        <input name="id" id="id" type="text" hidden bind:value={pat['id']} />
        <div class="row g-2 align-items-center">
          <div class="col-auto">
            <label for="name">Nome:</label>
          </div>
          <div class="col-md-6">
            <input id="name" name="name" required bind:value={pat['name']} class="form-control" />
          </div>
        </div>
        <div class="row g-2 align-items-center">
          <div class="col-auto">
            <label for="cpf">CPF:</label>
          </div>
          <div class="col-md-6">
            <input
              id="cpf"
              name="cpf"
              minlength="14"
              required
              bind:value={pat['cpf']}
              class="form-control"
              use:imask={options.cpf}
            />
          </div>
        </div>
        <div class="row g-2 align-items-center">
          <div class="col-auto">
            <label for="birthdate">Data de Nascimento:</label>
          </div>
          <div class="col-md-6">
            <input
              type="date"
              id="birthdate"
              name="birthdate"
              on:keyup={() => {
                dateIsValid;
              }}
              minlength="10"
              required
              bind:value={pat['birth_date']}
              class="form-control"
            />
            {#if !validDate}
              <p class="error">Data inválida</p>
            {/if}
          </div>
        </div>
        <div class="row g-2 align-items-center">
          <div class="col-auto">
            <label for="gender">Sexo:</label>
          </div>
          <div class="col-md-2">
            <select id="gender" name="gender" bind:value={pat['sex']} class="form-control">
              {#each gen as g}
                <option value={g.value}>{g.text}</option>
              {/each}
            </select>
          </div>
        </div>

        <div class="row g-2 align-items-center">
          <div class="col-auto">
            <label for="status">Status:</label>
          </div>
          <div class="col-md-2">
            <select id="status" name="status" bind:value={pat['status']} class="form-control">
              {#each stat as s}
                <option value={s.value}>{s.text}</option>
              {/each}
            </select>
          </div>
        </div>
        <a href="/records">
          <button on:click class="btn btn-outline-danger">Cancelar</button>
        </a>
        <button class="btn btn-success" on:click={onClickUpdate} disabled={!validDate}>Edit</button>
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
    height: 60%;
  }

  form {
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
    text-align: right;
  }
  .error {
    color: red;
  }
</style>
