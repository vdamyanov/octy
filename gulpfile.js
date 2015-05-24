var gulp = require('gulp');
var requireDir = require('require-dir');
var dir = requireDir('./tasks');
var paths = require('./tasks/paths');
var path = require('path');
var del = require('del');
var nodemon = require('gulp-nodemon');

var watching = false;
gulp.task('watch', ['assets'], function(){
  watching = true;
  gulp.watch(paths.scripts.concat(paths.templates), ['scripts']);
  gulp.watch(paths.styles.paths, ['styles']);

  gulp.watch(['bower.json'], ['vendor-scripts']);
});

gulp.task('clean', function (cb) {
  //  Don't clean when watching files.
  if (watching) return cb();

  return del('build/*', cb);
});

gulp.task('nodemon', function () {
  nodemon({
    script: 'proxy-server/server.js',
    watch: ['proxy-server'],
    ext: 'js'
  })
  .on('restart', function () {
    console.log('Server restarted!');
  });
});

gulp.task('build', ['assets']);
gulp.task('default', ['nodemon', 'watch']);
