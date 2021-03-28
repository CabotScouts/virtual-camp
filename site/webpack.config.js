const path = require('path');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

module.exports = {
  entry: ["./src/app.js", "./src/scss/style.scss"],
  output: {
    path: path.resolve(__dirname, 'static'),
    filename: 'app.js'
  },
  module: {
    rules: [
      {
      test: /\.(scss)$/,
      use: [
        MiniCssExtractPlugin.loader, 'css-loader',
      {
        loader: 'postcss-loader', // Run post css actions
        options: {
          plugins: function () { // post css plugins, can be exported to postcss.config.js
            return [
              require('precss'),
              require('autoprefixer')
            ];
          }
        }
      }, {
        loader: 'sass-loader' // compiles Sass to CSS
      }]
    },
    {
      test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
      use: [
        {
          loader: 'file-loader',
          options: {
            name: '[name].[ext]',
            outputPath: 'webfonts/'
          }
        }
      ]
    }]
  },
  optimization: {
    minimizer: [
      new UglifyJsPlugin({
        cache: true,
        parallel: true,
        sourceMap: false
      }),
      new OptimizeCSSAssetsPlugin({
        cssProcessorPluginOptions: {
          preset: ['default', { discardComments: { removeAll: true } }],
        }
      })
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      // path: path.resolve(__dirname, 'site/static'),
      filename: '[name].css',
      chunkFilename: '[id].css',
    }),
  ],
};
