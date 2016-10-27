/**
 * Created by jasonwirth on 9/7/16.
 */

$( document ).ready(function(){
    // $(".button-collapse").sideNav();
    $('.button-collapse').sideNav({
      // menuWidth: 300, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    }
  );
});

var app = angular.module("sherpa", ['ui.router', 'ui.materialize']);


app.controller('mainCtrl', function($scope, userService){
    console.log("mainCtrl loaded");
    $scope.userService = userService;

});

app.service('userService', function () {
    this.name = 'Steve Stone'
});


