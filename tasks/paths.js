module.exports = {
  scripts: ['webapp/**/*.js'],
  static: [
    'static/**',
    'static/*',
  ],
  styles: {
    paths: [
      'styles/*.styl',
      'styles/**/*.styl',
    ],
    source: '/styles/application.styl'
  },
  fonts: ['styles/fonts/*'],
  templates: ['webapp/**/*.html'],
  files: ['webapp/app.html'],
  dir: {
    build: './build/',
    assets: './build/assets/',
    static: './static/'
  }
};
