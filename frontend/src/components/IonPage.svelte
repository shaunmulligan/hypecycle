<script>
  import { fly, fade } from "svelte/transition";
</script>

<main in:fly={{ x: 200, duration: 250 }} out:fly={{ x: 200, duration: 250 }}>
  <slot />
</main>
