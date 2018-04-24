const config = require('./wp.config.js');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const extractSass = new ExtractTextPlugin({
    filename: "[name].[contenthash].css",
});

config.output.path = require('path').resolve('./assets');

module.exports = merge(config, {
        mode: 'production',

        module: {
            rules: [{
                test: /\.scss$/,
                use: extractSass.extract({
                    use: [{
                        loader: "css-loader"
                    }, {
                        loader: "sass-loader"
                    }],
                    fallback: "style-loader"
                })
            }]
        },

        plugins: [
            new BundleTracker({filename: './webpack-stats-prod.json'}),
            extractSass
        ]
    }
);
