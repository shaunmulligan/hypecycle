import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { terser } from 'rollup-plugin-terser';
import sveltePreprocess from 'svelte-preprocess';
import typescript from '@rollup/plugin-typescript';

import copy from 'rollup-plugin-copy';
import del from 'rollup-plugin-delete';

import postcss from 'rollup-plugin-postcss';
import json from "@rollup/plugin-json";

const production = !process.env.ROLLUP_WATCH;

const serve = () => {
    let server;

    function toExit() {
        if (server) server.kill(0);
    }

    return {
        writeBundle() {
            if (server) return;
            server = require('child_process').spawn('npm', ['run', 'start', '--', '--dev'], {
                stdio: ['ignore', 'inherit', 'inherit'],
                shell: true
            });

            process.on('SIGTERM', toExit);
            process.on('exit', toExit);
        }
    };
}

// because of fix on firebase/analytics, we get a circular reference on ionic
const onwarn = (warning, warn) => {
    if (warning.code === 'CIRCULAR_DEPENDENCY' && warning.importer.includes('@ionic')) {
        console.log('Supressed circular warning Ionic in rollup')
        return;
    } else {
        warn(warning);
    }
}

export default {
    onwarn,
    input: 'src/main.ts',
    output: {
        sourcemap: !production,
        format: 'esm',
        name: 'app',
        dir: 'public/bundle'
    },
    plugins: [
        production && del({ targets: 'public/bundle/*' }),

        copy({
            targets: [{ src: ['src/service-worker.js', 
            'src/manifest.json', 
            'src/index.html', 
            'src/global.css', 
            'src/favicon.png', 
            'node_modules/@ionic/core/css/ionic.bundle.css',
            'node_modules/@ionic/core/dist/ionic/',
            'src/assets'], dest: 'public/' }],
            verbose: true
        }),

        // no service worker in dev
        !production && del({ targets: 'public/service-worker.js' }),

        svelte({
            // enable run-time checks when not in production
            dev: !production,
            emitCss: true,
            // // we'll extract any component CSS out into
            // // a separate file - better for performance
            css: css => {
                css.write('bundle.css');
            },
            preprocess: sveltePreprocess(),
        }),

        // If you have external dependencies installed from
        // npm, you'll most likely need these plugins. In
        // some cases you'll need additional configuration -
        // consult the documentation for details:
        // https://github.com/rollup/plugins/tree/master/packages/commonjs
        resolve({
              browser: true,
              preferBuiltins: false,
              mainFields: ["main", "module"],
              dedupe: importee => importee === "svelte" || importee.startsWith("svelte/")
            }),

        commonjs(),
        json(),
        typescript({ sourceMap: !production }),
        postcss({
            extract: true
        }),

        // In dev mode, call `npm run start` once
        // the bundle has been generated
        !production && serve(),

        // If we're building for production (npm run build
        // instead of npm run dev), minify
        production && terser()
    ],
    watch: {
        clearScreen: false
    }
};