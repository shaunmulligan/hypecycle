<script>
  import { onMount } from "svelte";

  export let tabs;
  export let selected;

  console.log("Init IonTabs", tabs, selected);

  // ugly implmentation - to avoid present method not present
  // selected-tab does not seem to work
  let tries = 0;
  const selectTab = () => {
    const controller = document.querySelector("ion-tabs");
    if (controller.select) {
      controller.select(selected);
    } else if (tries < 300) {
      setTimeout(() => {
        tries++;
        selectTab();
      }, 1);
    }
  };

  onMount(() => {
    if (selected) {
      selectTab();
    }
  });

  const tabsChange = event => {
    console.log("Tabs change", event.detail.tab);

    // to support back button - some tries
    //  history.pushState(
    //    event.detail,
    //    event.detail.tab,
    //    "tabs/" + event.detail.tab
    //  );
    // console.log("History", window.history);
  };
</script>

<ion-router />
<ion-tabs on:ionTabsDidChange={tabsChange}>
  {#each tabs as tab}
    <ion-tab tab={tab.tab}>
      <svelte:component this={tab.component} />
    </ion-tab>
  {/each}

  <ion-tab-bar slot="bottom" selected-tab={selected}>
    {#each tabs as tab}
      <ion-tab-button tab={tab.tab}>
        <ion-label>{tab.label}</ion-label>
        <ion-icon name={tab.icon} />
      </ion-tab-button>
    {/each}

  </ion-tab-bar>
</ion-tabs>
