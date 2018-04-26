/* eslint-disable no-undef */
const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const DashboardPlugin = require('webpack-dashboard/plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const styles_path = 'css/[name].[hash].css';
const extractSass = new ExtractTextPlugin(styles_path, {
  allChuncks: true
});

const cssConfig = extractSass.extract({
  use: [
    {
      loader: 'css-loader',
      options: {sourceMap: true }
    },
    {
      loader: 'sass-loader',
      options: {sourceMap: true}
    }],
  fallback: 'style-loader'
});

const config = {
  context: __dirname,

  entry: {
    'themes': '../theme/static/theme/react/app.jsx',
  },

  output: {
    path: path.resolve('./static/bundles/'),
    filename: 'js/[name]-[hash].js',
    publicPath: '/static/bundles/'
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new DashboardPlugin({
      minified: false,
      gzip: false
    }),
    extractSass
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
        }
      },
      {
        test: /\.html$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'html-loader',
        }
      },
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader?cacheDirectory=true',
        }
      },
      {
        test: /\.scss$/,
        exclude: /node_modules/,
        use: cssConfig
      },
      {
        test: /\.jpe?g$|\.gif$|\.ico$|\.png$|\.svg$/,
        use: 'file-loader?name=[name].[ext]?[hash]'
      },

      {
        test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'url-loader?limit=10000&mimetype=application/font-woff'
      },

      {
        test: /\.(ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'file-loader'
      },
      {
        test: /\.otf(\?.*)?$/,
        use: 'file-loader?name=/fonts/[name].  [ext]&mimetype=application/font-otf'
      }

    ]
  },

  resolve: {
    modules: ['node_modules', 'bower_components'],
    extensions: ['.js', '.jsx', '.sass', '.less', '.scss'],
  },
};

module.exports = config;