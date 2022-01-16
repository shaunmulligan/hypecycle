<ion-label id=container>
    <h3>Time</h3>
    <h2>{hours}:{minutes}:{seconds}</h2>
</ion-label>

<script>
    import { onMount } from 'svelte';

    let time = new Date();

    // these automatically update when `time`
    // changes, because of the `$:` prefix
    $: hours = time.getHours().toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    $: minutes = time.getMinutes().toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    $: seconds = time.getSeconds().toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});

    onMount(() => {
        const interval = setInterval(() => {
            time = new Date();
        }, 1000);

        return () => {
            clearInterval(interval);
        };
    });
</script>

<style>
    #container {
      text-align: center;
      position: relative;
      left: 0;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      outline: 2px solid black;
    }
    
    #container h2 {
      font-size: 60px;
      line-height: 56px;
    }
    
    #container h3 {
      font-size: 22px;
      line-height: 32px;
      color: #8c8c8c;
      margin: 0;
    }
</style>