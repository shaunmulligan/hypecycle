<svelte:head>
  <title>Overkill Settings</title>
</svelte:head>

<ion-header translucent="true">
  <ion-toolbar>
    <ion-buttons slot="start">
      <ion-menu-button></ion-menu-button>
    </ion-buttons>
    <ion-title>Settings</ion-title>
    <ion-buttons slot="end">
      <ion-button on:click={showSimpleAlert}>
        <ion-icon slot="icon-only" name="power" color="danger"></ion-icon>
      </ion-button>
    </ion-buttons>
  </ion-toolbar>
</ion-header>

<ion-content fullscreen>
  <ion-list>
    <ion-item>
      <ion-label>
        <ion-text>Screen</ion-text>
      </ion-label>
      <ion-range min="40" max="250" step="2" value={screenBrightness} on:ionChange={setScreenBrightness}>
        <ion-icon size="small" slot="start" name="sunny"></ion-icon>
        <ion-icon slot="end" name="sunny"></ion-icon>
      </ion-range>
    </ion-item>
    <ion-item>
      <ion-label>Power Saving Mode</ion-label>
      <ion-toggle checked={powerMode} on:ionChange={setPowerMode}></ion-toggle>
    </ion-item>
    <ion-item>
      <ion-icon slot="start" name="wifi"></ion-icon>
      <ion-label>Wifi</ion-label>
      <ion-toggle checked={wifiState} on:ionChange={setWifiState}></ion-toggle>
    </ion-item>
    <ion-item>
      <ion-icon slot="start" name="bluetooth"></ion-icon>
      <ion-label>Bluetooth</ion-label>
      <ion-toggle checked={bluetoothState} on:ionChange={setBluetoothState}></ion-toggle>
    </ion-item>
    <ion-item>
      <ion-icon slot="start" name="cloud-upload"></ion-icon>
      <ion-label>Auto Upload</ion-label>
      <ion-toggle checked={autoUploadState} on:ionChange={setAutoUploadState}></ion-toggle>
    </ion-item>
    <ion-item-divider/>
  </ion-list>
  <ion-list >
    <ion-list-header>Connected Sensors</ion-list-header>

    {#each registeredSensorList as sensor}
      <RegisteredSensor name={sensor.name} icon={sensor.icon} protocol={sensor.protocol} />
    {/each}
    <ion-item lines="none" />
  </ion-list>

  <ion-button expand="full" color="primary" on:click={addSensorModal}>
    Add Sensor
  </ion-button>
</ion-content>

<script>
  import SensorsModal from "../../components/DiscoveredSensorsModal.svelte";
  import { IonicShowModal,IonicShowAlert } from "../../services/IonicControllers";
  import RegisteredSensor from "../../components/RegisteredSensor.svelte";

  let registeredSensorList = [
    {
      name: "Garmin HRM Pro",
      icon: "heart",
      type: "heartrate",
      protocol: "BLE",
    },
    {
      name: "4iii Power Meter",
      icon: "flash",
      type: "power",
      protocol: "BLE",
    },
  ];
  let powerMode = false;
  let wifiState = true;
  let bluetoothState = true;
  let screenBrightness = 150;
  let autoUploadState = true;

  const addSensorModal = () => {
    console.log("Adding Sensor")
    // Todo: make a call to /sensors/discover to get a list of available sensors and populate a modal with them.
    IonicShowModal("modal-extra", SensorsModal, 
    registeredSensorList ).then(console.log);
  }

  const showSimpleAlert = () => {
    IonicShowAlert({
      header: "Shutdown",
      message: "Are you sure you want to shutdown?",
      buttons: [{
        text: 'OK',
        role: 'OK',
        handler: () => {
          console.log('OK clicked');
          // Todo: Make call to API for shutdown
        }
      },
      {
        text: 'Cancel',
        handler: () => {
          console.log('Cancel clicked');
        }
      }],
    });
  };
  const setPowerMode = (e) => {
    // Connect this to a store which calls the API to set the power mode
    powerMode = e.detail.checked;
    console.log("Power Mode:", powerMode);
  }

  const setWifiState = (e) => {
    // Connect this to a store which calls the API to set the wifi state
    wifiState = e.detail.checked;
    console.log("Wifi State:", wifiState);
  }

  const setBluetoothState = (e) => {
    // Connect this to a store which calls the API to set the bluetooth state
    bluetoothState = e.detail.checked;
    console.log("Bluetooth State:", bluetoothState);
  }

  const setAutoUploadState = (e) => {
    // Connect this to a store which calls the API to set the auto upload state
    autoUploadState = e.detail.checked;
    console.log("Auto Upload State:", autoUploadState);
  }

  const setScreenBrightness = (event) => {
    // Connect this to a store which calls the API to set the screen brightness
    screenBrightness = event.detail.value;
    console.log("Screen level : " + event.detail.value);
  }

</script>