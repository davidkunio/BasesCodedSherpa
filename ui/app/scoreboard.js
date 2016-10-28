function mlbGamesCtrl($scope, socketService, gameService) {
    $scope.gameService = gameService;
    $scope.socketService = socketService;
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

    $scope.joinGame = function (game){
        $scope.socketService.connectSocket(game.url);
        console.log('Joining game: ' + game.url);
    };
}

app.service('gameService', function () {
    this.getGames = function(){
        var games = data.score_card.data.games.game.slice([1]);
        return games;
    }
});
