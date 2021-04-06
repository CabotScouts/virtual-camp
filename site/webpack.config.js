const path = require('path');
const TerserPlugin = require("terser-webpack-plugin");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CSSMinimizerPlugin = require('css-minimizer-webpack-plugin');

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
      use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
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
      new TerserPlugin(),
      new CSSMinimizerPlugin()
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css',
    }),
  ],
};
