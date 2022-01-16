<ion-label id=container>
    <h3>Timer</h3>
    <h2>{h}:{m}:{s}</h2>
</ion-label>

<script>

    export let seconds;
    seconds = Number(seconds);
    $: h = Math.floor(seconds % (3600*24) / 3600).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    $: m = Math.floor(seconds % 3600 / 60).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    $: s = Math.floor(seconds % 60).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
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