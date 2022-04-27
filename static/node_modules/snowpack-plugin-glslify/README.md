# snowpack-plugin-glslify

[![NPM Package][npm]][npm-url]

Import GLSL code with [glslify](https://github.com/glslify/glslify) (a node.js-style module system for GLSL).

```js
import frag from './shaders/frag.glsl'
console.log(frag)
```

## Installation

```sh
npm install --save-dev snowpack-plugin-glslify
```
```sh
yarn add -D snowpack-plugin-glslify
```

## Usage

```js
// snowpack.config.js
import glslify from 'snowpack-plugin-glslify'

export default {
  // ...
  plugins: [
    'snowpack-plugin-glslify'
  ]
}
```

## Options

Currently, the only supported option is compress.
If you need more, shoot me a PR. 

```js
  plugins: [
    ['snowpack-plugin-glslify', { "compress": false }]
  ]
```

## License

Released under the [MIT license](LICENSE).

[npm]: https://img.shields.io/npm/v/snowpack-plugin-glslify.svg
[npm-url]: https://www.npmjs.com/package/snowpack-plugin-glslify