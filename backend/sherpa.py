from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from handlers import handlers
from statcastdata import StatCastData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=None)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

def background_thread():
    print("started thread")
    game_id = 1234
    er = StatCastData(game_id)
    while True:
        before, event, after = er.getEvent()
        if not state or not event:
            break

        #socketio.emit('state_event', {'state': state, 'event': event})
        print(before, event, after)

        sherpa_messages = filter(lambda x: x is not None,
                                [handler(before, event, after) for handler in handlers])

        for message in sherpa_messages:
            socketio.emit('sherpa_message', message)

        socketio.sleep(10)



if __name__ == '__main__':
    print("here?")

    thread = socketio.start_background_task(target=background_thread)

    socketio.run(app, debug=True)
