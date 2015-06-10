var path = require('path');
var cacheBust = require('gulp-cache-bust');
var gulp = require('gulp');
var gutil = require('gulp-util');
var bowerFiles = require('main-bower-files');
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');
var minifycss = require('gulp-minify-css');
var stylus = require('gulp-stylus');
var order = require('gulp-order');
var concat = require('gulp-concat');
var paths = require('./paths');
var autoprefixer = require('gulp-autoprefixer');
var merge = require('gulp-merge');
var sourcemaps = require('gulp-sourcemaps');
var templateCache = require('gulp-angular-templatecache');
var flatten = require('gulp-flatten');
var plumber = require('gulp-plumber');
var ngAnnotate = require('gulp-ng-annotate');

var buildDir = paths.dir.build;
var assetsDir = paths.dir.assets;

gulp.task('scripts', ['clean'], function () {
  return merge(

    // Application code

    gulp.src(paths.scripts)
      .pipe(order([
        'app.js',
        'services/*.js',
        'pages/**/*Routes.js',
        '*.js'
      ])),

    // Template caching

    gulp.src(paths.templates)
      .pipe(flatten())
      .pipe(templateCache({module: 'unata', base: ''}))
      .pipe(gutil.noop()) // FIXME: Why is this necessary?!
  )
  .pipe(jshint({
    strict: false,        // Ignore errors about function scope strict mode
    globalstrict: true,   // Ignore errors about using a global strict declaration
    globals: {            // Globals not declared in the app code
      angular: true,
      _: true,
      console: true
    },
    browser: true,        // We're running in a browser environment, whitelist some more globals
    laxbreak:true         // Allow multiple line expressions
  }))
  .pipe(jshint.reporter('default'))
  .pipe(ngAnnotate())
  .pipe(sourcemaps.init())
  .pipe(concat('application.js', {newLine: '\n;\n'}))
  // .pipe(uglify())
  // .pipe(sourcemaps.write('sourcemaps'))
  .pipe(gulp.dest(assetsDir + 'js'));
});

gulp.task('styles', ['clean'], function () {
  return gulp.src(paths.styles.source)
    .pipe(plumber())
    .pipe(stylus())
    .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 9', 'ie_mob', 'bb', 'opera 12.1', 'ios 6', 'android 4'))
    .pipe(concat('application.css'))
    .pipe(gulp.dest(assetsDir + 'css'));
});

gulp.task('fonts', ['clean'], function () {
  return gulp.src(paths.fonts)
    .pipe(gulp.dest(assetsDir + 'fonts'));
});

//-- Vendor Dependencies Processing -----------------------------------------

gulp.task('vendor-scripts', ['clean'], function () {
  return gulp.src(bowerFiles())
    .pipe(concat('vendor.js', {newLine: '\n;\n'}))
    // .pipe(uglify())
    .pipe(gulp.dest(assetsDir + 'js'));
});

gulp.task('files', ['clean'], function () {
  return gulp.src(paths.files)
    .pipe(cacheBust({
      type: 'timestamp'
    }))
    .pipe(gulp.dest(buildDir));
});

gulp.task('publish-static', function() {
  return gulp.src(paths.static)
    .pipe(gulp.dest(buildDir));
});

gulp.task('assets', [
  'files',
  'scripts',
  'styles',
  'fonts',
  'vendor-scripts',
  'publish-static'
]);