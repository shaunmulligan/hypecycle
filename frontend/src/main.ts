import App from './App.svelte';

import { routes } from "./routes/routes";

import 'leaflet/dist/leaflet.css';

const app = new App({
	target: document.body,
	props: {
		routes
	}
});

export default app;