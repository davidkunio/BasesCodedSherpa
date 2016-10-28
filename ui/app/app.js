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


app.controller('mainCtrl', function($scope, userService, socketService, gameService){
    console.log("mainCtrl loaded");
    $scope.userService = userService;
    $scope.socketService = socketService;
    $scope.gameService = gameService;

    socketService.scope = $scope;

});

function mlbGamesCtrl($scope, socketService, gameService) {
    $scope.gameService = gameService;
    $scope.search = '';
    $scope.searchFilter = function (game){
        if( game.home_team_name.toLocaleLowerCase().indexOf( $scope.search.toLowerCase() ) > -1) {
            return true;
        }
        if( game.away_team_name.toLocaleLowerCase().indexOf( $scope.search.toLowerCase() ) > -1) {
            return true;
        }
        return false;
    };
}

function miniGamesCtrl($scope, socketService, miniGameService)  {
    $scope.miniGameService = miniGameService;
}

app.service('userService', function () {
    this.user = data.user;
});

app.filter('reverse', function() {
    return function(items) {
        return items.slice().reverse();
    };
});

app.service('gameService', function () {
   this.getGames = function(){
       var games = data.score_card.data.games.game.slice([1]);
       return games;
   }
});


app.service('miniGameService', function(){
    this.games = ['a', 'b', 'c'];
});


function messagesCtrl($scope, $rootScope, userService, socketService) {
    $scope.socketService = socketService;
    console.log(socketService.messages);

    // $scope.$watch("socketService.messages", function() {
    //     $scope.$apply()
    // }, true);
}

app.service('socketService', function () {
    // Use a "/test" namespace.
    // An application can open a connection on multiple namespaces, and
    // Socket.IO will multiplex all those connections on a single
    // physical channel. If you don't care about multiple channels, you
    // can set the namespace to an empty string.
    var that = this;
    that.messages = [{data: "Default message"}];
    this.namespace = '';
    this.port = '5000';
    this.domain = '127.0.0.1';
    console.log("Connecting socketService");

    this.getMessages = function(){
        return messages;
    };
    // Connect to the Socket.IO server.
    // The connection URL has the following format:
    //     http[s]://<domain>:<port>[/<namespace>]
    var socket = io.connect('http://' + this.domain + ':' + this.port + this.namespace);
    this.socket = socket;
    // Event handler for new connections.
    // The callback function is invoked when a connection with the
    // server is established.
    socket.on('connect', function() {
        socket.emit('my_event', {data: 'I\'m connected!'});
        console.log('Connected');
    });

    socket.on('my_response', function(msg) {
        $('#log').append('<br>' + $('<div/>').text('Received #' + msg.count + ': ' + msg.data).html());
        console.log('Message: ' + msg.data);
        that.messages = that.messages.concat([msg]);
        that.scope.messages = that.messages;
        that.scope.$apply();
    });


})