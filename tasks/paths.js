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
  templates: ['app/**/*.html'],
  files: ['app/index.html'],
  dir: {
    build: './build/',
    assets: './build/assets/',
    static: './static/'
  }
};
