<svelte:head>
  <link
    rel="stylesheet"
    href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
  />
</svelte:head>
<script>
  import {onMount} from "svelte";
  import { LeafletMap, TileLayer, Marker} from 'svelte-leafletjs';
  const mapOptions = {
      center: [41.483561819705194, 2.214374347050403],
      zoom: 14,
  };

  const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
  const tileLayerOptions = {
      minZoom: 0,
      maxZoom: 20,
      maxNativeZoom: 19,
      attribution: "© OpenStreetMap contributors",
  };

  function onMapLoad(map) {
      console.log("Map loaded");
  }
  let leafletMap;
  onMount(() => {
      let map = leafletMap.getMap();
      map.whenReady(onMapLoad);
  });
</script>

<ion-header translucent="true">
    <ion-toolbar>
        <ion-buttons slot="start">
        <ion-menu-button></ion-menu-button>
        </ion-buttons>
        <ion-title>Navigation</ion-title>
    </ion-toolbar>
</ion-header>

<div class="example" >
  <LeafletMap bind:this={leafletMap} options={mapOptions} >
      <TileLayer url={tileUrl} options={tileLayerOptions} />
      <Marker latLng={mapOptions.center}/>
  </LeafletMap>
</div>

<style>
  .example{
    height: 100%;
  width: 100%;
}
</style>