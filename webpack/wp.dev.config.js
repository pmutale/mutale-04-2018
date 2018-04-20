const path = require('path');
const config = require('./wp.config');
const merge = require('webpack-merge');
const webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const styles_path = path.resolve('../static/bundles/css/[name].[hash].css');

const extractSass = new ExtractTextPlugin(styles_path, {
    allChuncks: true
});



module.exports = merge(config, {
    // devtool: 'source-map',
    mode: 'development',

    devServer: {
        hot: true,
        inline: true,
        port: 4040,
        host:"mutale.localhost",
        proxy: {
            '**': 'http://localhost:4000'
        }
    },

    plugins: [
        extractSass,
    ]
} );
