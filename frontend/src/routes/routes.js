
/**
 * @roxi/routify 2.1.2
 * File generated Sun Jan 16 2022 15:00:07 GMT+0000 (Greenwich Mean Time)
 */

export const __version = "2.1.2"
export const __timestamp = "2022-01-16T15:00:07.221Z"

//buildRoutes
import { buildClientTree } from "@roxi/routify/runtime/buildRoutes"

//imports


//options
export const options = {}

//tree
export const _tree = {
  "name": "_layout",
  "filepath": "/_layout.svelte",
  "root": true,
  "ownMeta": {},
  "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/_layout.svelte",
  "children": [
    {
      "isFile": true,
      "isDir": false,
      "file": "_fallback.svelte",
      "filepath": "/_fallback.svelte",
      "name": "_fallback",
      "ext": "svelte",
      "badExt": false,
      "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/_fallback.svelte",
      "importPath": "../pages/_fallback.svelte",
      "isLayout": false,
      "isReset": false,
      "isIndex": false,
      "isFallback": true,
      "isPage": false,
      "ownMeta": {},
      "meta": {
        "preload": false,
        "prerender": true,
        "precache-order": false,
        "precache-proximity": true,
        "recursive": true
      },
      "path": "/_fallback",
      "id": "__fallback",
      "component": () => import('../pages/_fallback.svelte').then(m => m.default)
    },
    {
      "isFile": true,
      "isDir": false,
      "file": "Activity.svelte",
      "filepath": "/Activity.svelte",
      "name": "Activity",
      "ext": "svelte",
      "badExt": false,
      "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/Activity.svelte",
      "importPath": "../pages/Activity.svelte",
      "isLayout": false,
      "isReset": false,
      "isIndex": false,
      "isFallback": false,
      "isPage": true,
      "ownMeta": {},
      "meta": {
        "preload": false,
        "prerender": true,
        "precache-order": false,
        "precache-proximity": true,
        "recursive": true
      },
      "path": "/Activity",
      "id": "_Activity",
      "component": () => import('../pages/Activity.svelte').then(m => m.default)
    },
    {
      "isFile": true,
      "isDir": false,
      "file": "index.svelte",
      "filepath": "/index.svelte",
      "name": "index",
      "ext": "svelte",
      "badExt": false,
      "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/index.svelte",
      "importPath": "../pages/index.svelte",
      "isLayout": false,
      "isReset": false,
      "isIndex": true,
      "isFallback": false,
      "isPage": true,
      "ownMeta": {},
      "meta": {
        "preload": false,
        "prerender": true,
        "precache-order": false,
        "precache-proximity": true,
        "recursive": true
      },
      "path": "/index",
      "id": "_index",
      "component": () => import('../pages/index.svelte').then(m => m.default)
    },
    {
      "isFile": true,
      "isDir": false,
      "file": "Navigate.svelte",
      "filepath": "/Navigate.svelte",
      "name": "Navigate",
      "ext": "svelte",
      "badExt": false,
      "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/Navigate.svelte",
      "importPath": "../pages/Navigate.svelte",
      "isLayout": false,
      "isReset": false,
      "isIndex": false,
      "isFallback": false,
      "isPage": true,
      "ownMeta": {},
      "meta": {
        "preload": false,
        "prerender": true,
        "precache-order": false,
        "precache-proximity": true,
        "recursive": true
      },
      "path": "/Navigate",
      "id": "_Navigate",
      "component": () => import('../pages/Navigate.svelte').then(m => m.default)
    },
    {
      "isFile": false,
      "isDir": true,
      "file": "overkill",
      "filepath": "/overkill",
      "name": "overkill",
      "ext": "",
      "badExt": false,
      "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/overkill",
      "children": [
        {
          "isFile": true,
          "isDir": false,
          "file": "History.svelte",
          "filepath": "/overkill/History.svelte",
          "name": "History",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/overkill/History.svelte",
          "importPath": "../pages/overkill/History.svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": false,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "preload": false,
            "prerender": true,
            "precache-order": false,
            "precache-proximity": true,
            "recursive": true
          },
          "path": "/overkill/History",
          "id": "_overkill_History",
          "component": () => import('../pages/overkill/History.svelte').then(m => m.default)
        },
        {
          "isFile": true,
          "isDir": false,
          "file": "Map.svelte",
          "filepath": "/overkill/Map.svelte",
          "name": "Map",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/overkill/Map.svelte",
          "importPath": "../pages/overkill/Map.svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": false,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "preload": false,
            "prerender": true,
            "precache-order": false,
            "precache-proximity": true,
            "recursive": true
          },
          "path": "/overkill/Map",
          "id": "_overkill_Map",
          "component": () => import('../pages/overkill/Map.svelte').then(m => m.default)
        },
        {
          "isFile": true,
          "isDir": false,
          "file": "Settings.svelte",
          "filepath": "/overkill/Settings.svelte",
          "name": "Settings",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/pi/Hypecycle/backend/frontend/src/pages/overkill/Settings.svelte",
          "importPath": "../pages/overkill/Settings.svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": false,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "preload": false,
            "prerender": true,
            "precache-order": false,
            "precache-proximity": true,
            "recursive": true
          },
          "path": "/overkill/Settings",
          "id": "_overkill_Settings",
          "component": () => import('../pages/overkill/Settings.svelte').then(m => m.default)
        }
      ],
      "isLayout": false,
      "isReset": false,
      "isIndex": false,
      "isFallback": false,
      "isPage": false,
      "ownMeta": {},
      "meta": {
        "preload": false,
        "prerender": true,
        "precache-order": false,
        "precache-proximity": true,
        "recursive": true
      },
      "path": "/overkill"
    }
  ],
  "isLayout": true,
  "isReset": false,
  "isIndex": false,
  "isFallback": false,
  "isPage": false,
  "isFile": true,
  "file": "_layout.svelte",
  "ext": "svelte",
  "badExt": false,
  "importPath": "../pages/_layout.svelte",
  "meta": {
    "preload": false,
    "prerender": true,
    "precache-order": false,
    "precache-proximity": true,
    "recursive": true
  },
  "path": "/",
  "id": "__layout",
  "component": () => import('../pages/_layout.svelte').then(m => m.default)
}


export const {tree, routes} = buildClientTree(_tree)

