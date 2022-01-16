<script>
  import MetricWidget from "../components/MetricWidget.svelte";
  import Timer from "../components/Timer.svelte";
  import websocketStore from "../services/socketStore";

  const initialValue = { power: 0, speed: 0, elapsedTime: 0, cadence: 0, avgSpeed: 0 };
  export const myStore = websocketStore("ws://localhost:5001/ws", initialValue, []);

  let state = $myStore;
  
</script>

<svelte:head>
  <title>Overkill Current Ride</title>
</svelte:head>

<ion-header translucent="true">
  <ion-toolbar>
    <ion-buttons slot="start">
      <ion-menu-button></ion-menu-button>
    </ion-buttons>
    <ion-title>Afternoon Ride</ion-title>
  </ion-toolbar>
</ion-header>
<ion-content fullscreen>
  <ion-grid>
    <ion-row>
      <ion-col>
        <div>
          <MetricWidget label="Speed" value={$myStore.speed} unit="km/h" />
        </div>
      </ion-col>
      <ion-col>
        <div>
          <MetricWidget label="Heart Rate" value={$myStore.heartrate} unit="bpm" />
        </div>
      </ion-col>
    </ion-row>
    <ion-row>
      <ion-col>
        <div>
          <MetricWidget label="3s Power" value={$myStore.power} unit="W" />
        </div>
      </ion-col>
    </ion-row>
    <ion-row>
      <ion-col>
        <div>
          <Timer seconds={$myStore.elapsedTime} />
        </div>
      </ion-col>
    </ion-row>
    <ion-row>
      <ion-col>
        <div>
          <MetricWidget label="Avg. Speed" value={$myStore.avgSpeed | initialValue.avgSpeed} unit="km/h" />
        </div>
      </ion-col>
      <ion-col>
        <div>
          <MetricWidget label="Cadence" value={$myStore.cadence | initialValue.cadence} unit="rpm" />
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
