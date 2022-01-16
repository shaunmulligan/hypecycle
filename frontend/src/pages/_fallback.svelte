<style>
.huge {
  font-size: 12rem;
}
.e404 {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
</style>

<script>
import { url } from "@roxi/routify";
</script>

<ion-header translucent="true">
  <ion-toolbar>
    <ion-buttons slot="start">
      <ion-menu-button></ion-menu-button>
    </ion-buttons>
    <ion-title>Page Not Found</ion-title>
  </ion-toolbar>
</ion-header>
<div class="e404">
  <div class="huge">404</div>
  <div class="big">
    Page not found.
    <!-- link to the parent folder of _fallback.svelte -->
    <a href="{$url('../')}">Go back</a>
  </div>
</div>
