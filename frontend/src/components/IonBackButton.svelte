<script>
  const nav = document.querySelector("ion-nav");

  export let color;
  export let disabled = false;
  export let icon;
  export let text;

  const isMd = document.querySelector("html").className.includes("md");
  if (!icon) {
    icon = isMd ? "arrow-back" : "arrow-back";
  }

  if (!text && isMd) {
    text = "Back";
  }

  if (!color) {
    color = "primary";
  }

  const popWindow = () => {
    if (!disabled) {
      if (nav) {
        nav.pop();
      } else {
        window.history.back();
      }
    }
  };
</script>

<ion-button on:click={popWindow}>
  <ion-icon name={icon} {color} />
</ion-button>
