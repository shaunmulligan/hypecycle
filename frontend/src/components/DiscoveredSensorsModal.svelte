<svelte:head>
  <title>Ionic Companion - Modal Extra</title>
</svelte:head>

<ion-header translucent="true">
  <ion-toolbar>
    <ion-title>Avaliable Sensors</ion-title>
    <ion-buttons slot="end">
      <ion-button on:click="{closeOverlay}">Close</ion-button>
    </ion-buttons>
  </ion-toolbar>
</ion-header>
<ion-content fullscreen>
    <ion-list>
    
        {#each availableSensorsList as sensor, id}
            <ion-item>
                <ion-icon slot="start" name={sensor.icon}>
                </ion-icon>
                <ion-label>
                    <h2>{sensor.name}</h2>
                    <h3>{sensor.address}</h3>
                </ion-label>
                <ion-checkbox
                value={id}
                slot="end"
                checked={sensor.checked}
                on:ionChange={checkBoxChange} />
            </ion-item>
        {/each}
        <ion-item lines="none"/>
    </ion-list>
    <ion-button expand="full" on:click="{regSensors}">
        Register Sensors
    </ion-button>
</ion-content>

<script>
    // import DiscoveredSensor from "../../components/DiscoveredSensor.svelte";
    let overlayElement = document.querySelector("ion-modal");
    console.log(overlayElement.componentProps);

    // TODO: hook in real data from /sensors/discover
    let availableSensorsList = [
        {
        name: "Garmin HRM Tri",
        icon: "heart",
        type: "heartrate",
        protocol: "BLE",
        address: "00:00:00:00:00:00",
        checked: false
        },
        {
        name: "PowerTap Power Meter",
        icon: "flash",
        type: "power",
        protocol: "BLE",
        address: "00:00:00:00:00:00",
        checked: false
        },
        {
        name: "Tacx Neo Trainer",
        icon: "flash",
        type: "power",
        protocol: "BLE",
        address: "00:00:00:00:00:00",
        checked: false
        }
    ];
    
    const checkBoxChange = event => {
        if (event.detail.value) {
            console.log(event.detail.value)
            availableSensorsList[event.detail.value].checked = event.detail.checked;
        }
    };

    const regSensors = () => {
        // Todo: only activate regSensor button if at least one item is checked.
        console.log("registering Sensors");
        console.log(availableSensorsList);
        // TODO: register sensors that are checked on the /sensors/register endpoint
        closeOverlay();
    };

    const closeOverlay = () => {
        overlayElement.dismiss({ data: Date.now() });
    };
</script>
