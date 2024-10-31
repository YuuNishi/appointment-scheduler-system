<script lang="ts">
  import 'iconify-icon'

  function handleIconClick(iconName: string) {
    console.log(`Ícone clicado: ${iconName}`);
  }
</script>

<div class="sidebar">
  <div class="icon-div" on:click={() => handleIconClick('calendar')}>
    <iconify-icon icon="mdi:calendar-outline" width="36" height="36" class="icon"/>
  </div>
  <div class="icon-div" on:click={() => handleIconClick('records')}>
    <iconify-icon icon="cuida:user-add-outline" width="36" height="36" class="icon"/>
  </div>
  <div class="icon-div" on:click={() => handleIconClick('settings')}>
    <iconify-icon icon="material-symbols:settings-outline" width="36" height="36" class="icon"/>
  </div>
</div>

<style>
  .sidebar {
    padding: 1px;
    background-color: #007BFF;
    width: 64px;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .icon-div {
    display: flex;
    padding: 10px;
    margin: 0 0 10px 0;
    cursor: pointer;
    transition: color 0.3s;
  }

  .icon-div:hover {
    background-color:rgba(255, 255, 255, 0.329);
  }

  .icon {
    color: white;
  }
</style>
