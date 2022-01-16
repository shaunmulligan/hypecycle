<ion-menu
  side="{side}"
  content-id="main"
  menu-id="mainmenu"
>
  {#if menuItems.length > 0}
    <ion-header>
      <ion-toolbar translucent="true">
        <ion-title>Menu</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <ion-list>
        {#each menuItems as menuItem, i}
          <ion-item class="ion-padding"
            on:click="{() => {
              closeAndNavigate(menuItem.url);
            }}"
          >
            <ion-icon
              name="{menuItem.icon}"
              slot="start"
            ></ion-icon>
            <ion-label>{menuItem.label}</ion-label>
          </ion-item>
        {/each}

      </ion-list>
    </ion-content>
  {/if}
</ion-menu>

<style>
ion-item {
  cursor: pointer;
}
ion-icon{
  font-size: 25px!important
}
ion-label{
  font-size: 30px!important
}
</style>

<script lang="ts">
import { goto } from "@roxi/routify";
import { getIonicMenu } from "./../services/IonicControllers";
import { path } from "../services/routestore";

export let side = "start";

let menuItems = [{url: "/", label: "Home", icon:"home"},
                 {url: "/overkill/Map", label: "Map", icon:"map"},
                 {url: "/overkill/History", label: "History", icon:"book"},                
                 {url: "/overkill/Settings", label: "Settings", icon:"settings"}
                 
]

const closeAndNavigate = (url) => {
  console.log("Navigate url", url);

  path.set(url);
  $goto(url);

  getIonicMenu("mainmenu")
    .close(true)
    .then(() => {});
};

</script>
