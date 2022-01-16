<ion-label id=container>
    <h3>{label}</h3>
    <h2>{value}</h2>
    <h3>{unit}</h3>
</ion-label>

<script>
    export let label = "--"
    export let value = 0
    export let unit = ""
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