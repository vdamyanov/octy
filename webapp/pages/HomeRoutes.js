angular.module('octy').config(function($stateProvider, $urlRouterProvider) {
  $stateProvider.state('home', {
    url: '/',
    templateUrl: "home.html",
    controller: 'HomeController'
  });

  $urlRouterProvider.when('', '/');
});