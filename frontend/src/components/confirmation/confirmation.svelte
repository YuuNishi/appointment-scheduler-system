<script>
    export let confirm
</script>
<div class="modal">
    <div class="content">
        <form method="post" action="?/deletePatient">
            <p>Deseja mesmo excluir este paciente?</p>
            <button type="submit">Sim</button>
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
</style>
