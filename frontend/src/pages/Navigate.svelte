<script>
  import MetricWidget from "../components/MetricWidget.svelte";
  import Clock from "../components/Clock.svelte";
  import websocketStore from "../services/socketStore";

  const initialValue = { power: 0, speed: 0, elapsedTime: 0, cadence: 0, avgSpeed: 0 };
  export const myStore = websocketStore("ws://localhost:5001/ws", initialValue, []);
  // receive JSON from server (push)
  let state = $myStore;
  
  function secondsToHms(seconds) {
    seconds = Number(seconds);
    var h = Math.floor(seconds % (3600*24) / 3600).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    var m = Math.floor(seconds % 3600 / 60).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    var s = Math.floor(seconds % 60).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});

    return h + ':' + m +':' + s;
  }
</script>

<svelte:head>
  <title>Overkill Environmental</title>
</svelte:head>

<ion-header translucent="true">
  <ion-toolbar>
    <ion-buttons slot="start">
      <ion-menu-button></ion-menu-button>
    </ion-buttons>
    <ion-title>Environmental Data</ion-title>
  </ion-toolbar>
</ion-header>
<ion-content fullscreen>
  <ion-grid>
    <ion-row>
      <ion-col>
        <div>
          <MetricWidget label="Temperature" value=23.7 unit="℃" />
        </div>
      </ion-col>
      <ion-col>
        <div>
          <MetricWidget label="Gradient" value=7.1 unit="%" />
        </div>
      </ion-col>
    </ion-row>
    <ion-row>
      <ion-col>
        <div>
          <MetricWidget label="Accumulated Altitude" value=1456 unit="m" />
          <!-- Replace with HR + cource profile graph -->
        </div>
      </ion-col>
    </ion-row>
    <ion-row>
      <ion-col>
        <div>
          <Clock />
        </div>
      </ion-col>
    </ion-row>
    <ion-row>
      <ion-col>
        <div>
          <MetricWidget label="Avg. Power" value=210 unit="W" />
        </div>
      </ion-col>
      <ion-col>
        <div>
          <MetricWidget label="Place holder" value={$myStore.cadence | initialValue.cadence} unit="--" />
          <!-- Replace with Power zone distribution bar chart -->
        </div>
      </ion-col>
    </ion-row>
  </ion-grid>
</ion-content>

<style>
:root {
  --ion-safe-area-top: 20px;
  --ion-safe-area-bottom: 22px;
}
ion-col > div {
  background-color: #f7f7f7;
  border: solid 1px #ddd;
  padding: 10px;
}
</style>
