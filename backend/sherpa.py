from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from time import sleep
import random
import newrelic.agent

from handlers import handlers
from statcastdata import StatCastData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode="eventlet")

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

def background_thread():
    print("started thread")

    game_id = 1234
    scd = StatCastData()
    application = newrelic.agent.application()

    while True:
        with newrelic.agent.BackgroundTask(application, name="background", group='Task'):
            before, event, after = scd.return_update()
            if not before or not event or not after:
                break

            print(before, event, after)

            sherpa_messages = filter(lambda x: x is not None,
                                    [handler(before, event, after) for handler in handlers])

            for message in sherpa_messages:
                socketio.emit('sherpa_message', message)

        # sleep(random.uniform(.5,2))



if __name__ == '__main__':
    thread = socketio.start_background_task(target=background_thread)

    socketio.run(app, host="ec2-54-196-57-249.compute-1.amazonaws.com", port=80, debug=True)
