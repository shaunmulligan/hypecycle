<!-- This is the top level layout with menu -->
<svelte:head>
  <title>Ionic Companion - svelte power!</title>
</svelte:head>

<ion-app>

  {#if !activity.isRecording}
    <ion-fab horizontal="end" vertical="bottom" slot="fixed">
      <ion-fab-button on:click={startStopActivity}>
        <ion-icon name="caret-forward-circle"></ion-icon>
      </ion-fab-button>
    </ion-fab>
  {:else}
    <ion-fab horizontal="end" vertical="bottom" slot="fixed" >
      <ion-fab-button on:click={startStopActivity} color=danger>
        <ion-icon name="stop-circle"></ion-icon>
      </ion-fab-button>
    </ion-fab>
  {/if}

  <ion-split-pane content-id="main">
    <Menu />
    <div class="ion-page" id="main">
      <slot />
    </div>
  </ion-split-pane>
</ion-app>

<style>
@keyframes shadow-pulse {
  0% {
    box-shadow: 0 0 0 0px rgba(0, 0, 0, 0.2);
  }
  100% {
    box-shadow: 0 0 0 135px rgba(0, 0, 0, 0);
  }
}

</style>

<script>

import Menu from "../components/Menu.svelte";

let activity = {isRecording: false}

function startStopActivity() {
		console.log("Starting to record activity")
    activity.isRecording = !activity.isRecording;
    // TODO: check if an activity is already recording, if not then start a new one 
    // and change button to stop activity icon
}

</script>
