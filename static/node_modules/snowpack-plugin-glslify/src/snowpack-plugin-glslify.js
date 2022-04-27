const fs = require('fs').promises
const { dirname } = require('path')
const { compile } = require('glslify')

function compressShader(code) {
	let needNewline = false
	return code
		.replace(
			/\\(?:\r\n|\n\r|\n|\r)|\/\*.*?\*\/|\/\/(?:\\(?:\r\n|\n\r|\n|\r)|[^\n\r])*/g,
			''
		)
		.split(/\n+/)
		.reduce((result, line) => {
			line = line.trim().replace(/\s{2,}|\t/, ' ')
			if (line.charAt(0) === '#') {
				if (needNewline) {
					result.push('\n')
				}
				result.push(line, '\n')
				needNewline = false
			} else {
				result.push(
					line.replace(
						/\s*({|}|=|\*|,|\+|\/|>|<|&|\||\[|\]|\(|\)|-|!|;)\s*/g,
						'$1'
					)
				)
				needNewline = true
			}
			return result
		}, [])
		.join('')
		.replace(/\n+/g, '\n')
}

module.exports = function (snowpackConfig, pluginOptions) {
	const options = Object.assign(pluginOptions)

	return {
		name: 'my-snowpack-plugin',
		resolve: {
			input: ['.glsl', '.frag', '.vert'],
			output: ['.js'],
		},
		async load({ filePath }) {
			const fileOptions = Object.assign(
				{
					basedir: dirname(filePath),
				},
				options
			)

			let code = await fs.readFile(filePath, 'utf8')
			code = compile(code, fileOptions)
			if (options.compress !== false) {
				code = compressShader(code)
			}

			return `export default ${JSON.stringify(code)}`
		},
	}
}
