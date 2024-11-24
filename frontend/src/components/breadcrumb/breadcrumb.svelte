<script lang="ts">
  import type { BreadCrumbItemType } from '../../types/services/shared.types.js';

  let breadCrumbItems: BreadCrumbItemType[] = [];

  export { breadCrumbItems };
</script>


<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    {#each breadCrumbItems as breadCrumbItem}
      <li class="breadcrumb-item {breadCrumbItem.active && 'active'}">
        {#if !breadCrumbItem.active}
          <a href="{breadCrumbItem.route}">{breadCrumbItem.title}</a>
        {/if}
        {#if breadCrumbItem.active}
          {breadCrumbItem.title}
        {/if}
      </li>
    {/each}
  </ol>
</nav>