var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('unit', shell.task([
  'node_modules/karma/bin/karma start tests/unit/karma.conf.js --single-run'
], {ignoreErrors: true}));

gulp.task('unit:watch', shell.task([
  'node_modules/karma/bin/karma start tests/unit/karma.conf.js --no-single-run --auto-watch'
]));
