var express = require('express');
var path = require('path');
var app = express();
var httpProxy = require('http-proxy');
var gutil = require('gulp-util');

// Static files
app.use('/', express.static(path.join(__dirname, '..', 'build')));

// Set up api proxies
httpProxy.prototype.onError = function (err, req) {
  console.error(err, req.url);
};

var proxy = httpProxy.createProxyServer();

app.all('*', function(req, res) {
  req.headers.host = 'localhost:3000';
  proxy.web(req, res, {target: 'http://localhost:5000'});
});

gutil.log('API proxies initialized');

// Start server
var server = app.listen(3000, function() {
  var host = server.address().address;
  var port = server.address().port;

  gutil.log('Server listening at http://' + host + ':' + port);
});
