from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# Add any other events or routes here...

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    import eventlet
    import eventlet.wsgi

    if __name__ == '__main__':
        port = int(os.environ.get("PORT", 5000))
        eventlet.wsgi.server(eventlet.listen(('0.0.0.0', port)), app)

