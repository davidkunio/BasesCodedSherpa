
app.controller('mainCtrl', function($scope, userService, socketService, gameService){
    console.log("mainCtrl loaded");
    $scope.userService = userService;
    $scope.socketService = socketService;
    $scope.gameService = gameService;

    socketService.scope = $scope;

});


function miniGamesCtrl($scope, socketService, miniGameService)  {
    $scope.miniGameService = miniGameService;
    miniGameService.scope = $scope
}

app.service('miniGameService', function(){
    var that = this;
    that.gameHistory = function(){
        return [
            {
                gameId: '123',
                gameTitle: "Cubs vs Cardinals",
                gamesPlayed: []
            },
            {
                gameId: '123',
                gameTitle: "Cubs vs Marlins",
                gamesPlayed: []
            },
            {
                gameId: '123',
                gameTitle: "Cubs vs Dodgers",
                gamesPlayed: []
            }
        ];
    };

    that.current_games = [
        {
            title: 'Close Out',
            description: "Over-under on Champan ending the game in 17 pitches",
            answer: 'over',
            points: 100,
        },
        {
            title: 'Next Pitch',
            description: "Arrietta has thrown 10 straight curve balls.",
            answer: 'Fast ball, down the middle',
            points: 100,
        },
    ];

    that.addGame = function(msg, ans){
        var minigame = msg.minigame;
        minigame.answer = ans;
        console.log(that.current_games);
        that.current_games.push(minigame);
        that.scope.$apply();

    };

    that.leaderBoard = function(){
        return [
            {name: "Pete", wins: "50", losses: "50", percent: "50%"},
            {name: "Mickey", wins: "66", losses: "33", percent: "66%"},
            {name: "Bo", wins: "98", losses: "2", percent: "98%"},
        ];
    };
});
