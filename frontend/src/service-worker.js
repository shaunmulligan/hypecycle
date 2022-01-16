importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-sw.js');

console.log('Hello from service-worker.js!');

if (workbox) {
    console.log(`Yay! Workbox is loaded 🎉`, workbox.routing);
} else {
    console.log(`Boo! Workbox didn't load 😬`);
}