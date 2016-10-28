
function messagesCtrl($scope, $rootScope, userService, socketService, miniGameService) {
    $scope.socketService = socketService;
    $scope.miniGameService = miniGameService;
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
    that.messages = [
        {
            data: "Default message"
        },
        {
            title: "I have a minigame!",
            data: 'Message data',
            type: "minigame",
            text: "sacho.ul acthoeu satoehu satoehu satoeuhg ",
            minigame: {current_answer: null, choices: ["YES", "NO"]}
        },
        {
            title: "Update With Media",
            data: {
                text: "sacho.ul acthoeu satoehu satoehu satoeuhg ",
                media_type: 'image',
                media_url: 'http://sports.cbsimg.net/images/visual/whatshot/jake-arrieta-83015.jpg'
            },
            type: "update",
            text: "sacho.ul acthoeu satoehu satoehu satoeuhg ",
        }
        ];
    this.namespace = '';
    this.port = '5000';
    this.domain = '127.0.0.1';
    console.log("Connecting socketService");

    this.getMessages = function(){
        return messages;
    };

    this.removeMsg = function (msg) {
        that.messages = _.filter(that.messages, function (obj){
            return msg !== obj;
        });
        that.scope.$apply();
    };

    // Connect to the Socket.IO server.
    // The connection URL has the following format:
    //     http[s]://<domain>:<port>[/<namespace>]
    // var socket = io.connect('http://' + this.domain + ':' + this.port + this.namespace);


    that.connectSocket = function (url) {
        if ( url === undefined ){
            url = "http://127.0.0.1:5000/"
            console.log("Url is undefined. Using default value of: " + url);
        }
        var socket = io.connect(url);
        that.socket = socket;
        console.log("Connecting socket to: " + url);
        return socket;

    };

    var url = "http://ec2-54-196-57-249.compute-1.amazonaws.com:80/";
    that.connectSocket(url);
    // Event handler for new connections.
    // The callback function is invoked when a connection with the
    // server is established.
    that.socket.on('connect', function() {
        socket.emit('my_event', {data: 'I\'m connected!'});
        console.log('Connected');
    });

    that.socket.on('my_response', function(msg) {
        var d = new Date();
        msg.title = "Title " + d.toDateString() + " - " + Date.now().toString();
        $('#log').append('<br>' + $('<div/>').text('Received #' + msg.count + ': ' + msg.data).html());
        console.log('Message: ' + msg.data);
        that.messages = that.messages.concat([msg]);
        that.scope.messages = that.messages;
        that.scope.$apply();
    });


})
