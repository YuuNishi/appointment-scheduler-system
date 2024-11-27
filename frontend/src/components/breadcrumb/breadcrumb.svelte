<script lang="ts">
  import type { BreadCrumbItemType } from '../../types/services/shared.types.js';
  import { isDarkTheme } from '../../store/theme.store';

  let breadCrumbItems: BreadCrumbItemType[] = [];

  export { breadCrumbItems };
</script>

<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    {#each breadCrumbItems as breadCrumbItem}
      <li
        class="breadcrumb-item {breadCrumbItem.active && 'active'} {$isDarkTheme &&
          'breadcrumb-item-dark'}"
      >
        {#if !breadCrumbItem.active}
          <a href={breadCrumbItem.route}>{breadCrumbItem.title}</a>
        {/if}
        {#if breadCrumbItem.active}
          {breadCrumbItem.title}
        {/if}
      </li>
    {/each}
  </ol>
</nav>

<style>
  .breadcrumb-item-dark {
    color: white;
  }

  .breadcrumb-item-dark::before {
    color: white;
  }
</style>
