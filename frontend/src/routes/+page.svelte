<script lang="ts">
  import Sidebar from '../components/sidebar/sidebar.svelte';
  let isDarkMode : boolean;
</script>

<main>
  <Sidebar bind:isDarkMode/>
  <div class="content">
    <h1>Welcome to SvelteKit</h1>
    <p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
  </div>
</main>