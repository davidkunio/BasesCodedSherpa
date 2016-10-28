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



app.filter('reverse', function() {
    return function(items) {
        return items.slice().reverse();
    };
});
