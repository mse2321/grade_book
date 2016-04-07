var demo = angular.module('demo', ['ngRoute']);

	demo.config(['$routeProvider', function($routeProvider){
        $routeProvider.when('/', {
          templateUrl: 'intro.html',
          controller: 'ctrl'
        })
        .when('/login', {
          templateUrl: 'login.html',
          controller: 'ctrl'
        })
        .when('/dashboard', {
          templateUrl: 'dashboard.html',
          controller: 'ctrl'
        })
        .when('/grades', {
          templateUrl: 'grades.html',
          controller: 'ctrl'
        })
        .when('/settings', {
          templateUrl: 'settings.html',
          controller: 'ctrl'
        })
        .when('/import', {
          templateUrl: 'import.html',
          controller: 'ctrl'
        })
        .otherwise('/error',  {
          template: '<p>Error - Page Not Found</p>'
        });
     }])


demo.controller('ctrl', function(){
	
});
