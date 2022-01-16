<script>
  import { register } from "svelte-custom-elements";

  const isRegistered = function(name) {
    return document.createElement(name).constructor !== HTMLElement;
  };

  const registerWebComponentOnce = (selector, component) => {
    if (!isRegistered(selector)) {
      register(selector, component, []);
    }
  };

  export let component;
  export let animated;
  export let animation;
  export let root;
  export let rootParams;
  export let swipeGesture;

  registerWebComponentOnce(root, component);
</script>

<ion-nav
  on:ionNavDidChange
  on:ionNavWillChange
  {root}
  {animated}
  {animation}
  {rootParams}
  {swipeGesture} />
