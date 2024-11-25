<script lang="ts">
  import { onMount } from 'svelte';

  import "bootstrap/dist/css/bootstrap.min.css";
  import "./styles.css";

  onMount(async () => {
    if (typeof window !== "undefined") {
      await import("bootstrap/dist/js/bootstrap.bundle.js" as string);
    }
  });
</script>

<slot />