<script>
  import IonTab from "../components/IonTab.svelte";

  import Activity from "./Activity.svelte";
  import Navigate from "./Navigate.svelte";

  export let tab = "Activity";

  // too much?
  if (tab == ":tab") {
    tab = "Activity";
  }

  const myTabs = [
    { label: "Activity", icon: "bicycle", tab: "Activity", component: Activity },
    { label: "Data", icon: "bar-chart", tab: "Data", component: Navigate },
  ];

  console.log("Tabs", tab, myTabs);
</script>

<IonTab tabs={myTabs} selected={tab} />
