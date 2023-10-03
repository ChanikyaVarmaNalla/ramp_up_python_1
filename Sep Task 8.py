from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kingkong'
socketio = SocketIO(app)

@app.route('/user1')
def user1():
    return render_template('user1.html')

@app.route('/user2')
def user2():
    return render_template('user2.html')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = username
    join_room(room)
    emit('status', {'msg': f'{username} has joined.'}, room=room)

@socketio.on('text')
def handle_text(data):
    msg = data['msg']
    username = data['username']
    room = username

    # Emit the message to the sender's room
    emit('message', {'msg': msg, 'username': username}, room=room)

    # Broadcast the message to the other room (opposite user)
    other_room = 'User 2' if room == 'User 1' else 'User 1'
    emit('message', {'msg': msg, 'username': username}, room=other_room)

if __name__ == '__main__':
    socketio.run(app)
