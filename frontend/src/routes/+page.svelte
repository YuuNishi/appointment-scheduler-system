<script>
  import Sidebar from '../components/sidebar/sidebar.svelte';
</script>

<main>
  <Sidebar />
  <div class="content">
    <h1>Welcome to SvelteKit</h1>
    <p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
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
</style>
