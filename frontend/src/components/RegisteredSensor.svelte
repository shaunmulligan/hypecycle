<ion-item>
    <ion-icon slot="start" name={icon}>
    </ion-icon>
    <ion-label>
        <h2>{name}</h2>
        <h3>{protocol}</h3>
    </ion-label>
</ion-item>

<script>
    export let name = "UKNOWN"
    export let icon = "alert"
    export let protocol = "--"
    // Add battery level and connectivity status
</script>