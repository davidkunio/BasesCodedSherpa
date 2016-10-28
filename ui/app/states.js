
function profileCtrl($scope, $state, $stateParams, userService ){

}


// function listCtrl($scope, $state, $stateParams, listService ){
//     console.log("listCtrl loaded");
//     console.log($stateParams);
//     console.log($state.current);
//     // console.log(listService);
//     $scope.listService = listService;
//     $scope.$state = $state;
//
//     $scope.name = 'name';
//     // $scope.listFilter = $state.current.filter;
//     // $scope.listFilter = _.last($state.current.name.split('.'));
//     $scope.listFilter = $state.current.filter;
//
//     $scope.newRecipe = newRecipe();
//     $scope.listService.getRecipes();
//
//     $scope.saveMeal = function (){
//         listService.addRecipe($scope.newRecipe);
//         $scope.newRecipe = newRecipe();
//     };
// }


app.config(function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider.state('messages', {
        url: '/',
        templateUrl: 'app/templates/messages.tmpl.html',
        controller: messagesCtrl,
    });

    $stateProvider.state('mlb_games', {
        abstract: true,
        url: '/games',
        template: '<ui-view />'
    }).state('mlb_games.list', {
        url: '/list',
        controller: mlbGamesCtrl,
        templateUrl: 'app/templates/mlb_games.list.tmpl.html',
    }).state('mlb_games.details', {
        url: '/list',
        template: 'MLB Games Detail',
    });

    $stateProvider.state('mini_games', {
        abstract: true,
        url: '/games',
        template: '<ui-view />'
    }).state('mini_games.list', {
        url: '/list',
        templateUrl: 'app/templates/mini_games.list.tmpl.html',
        controller: miniGamesCtrl,
    }).state('mini_games.details', {
        url: '/list',
        template: 'Mini Games Detail',
    });

    $stateProvider.state('profile', {
        abstract: true,
        url: '/profile',
        template: '<ui-view />'
    })
        .state('profile.detail', {
            url: '/detail',
            controller: profileCtrl,
            // filter: 'thisWeek',
            template: 'Profile detail',
            // templateUrl: 'static/app/templates/list_page.tmpl',
        })
});