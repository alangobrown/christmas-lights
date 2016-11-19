from flask import render_template


from app import app

import socket
print(socket.gethostname())

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home', host=socket.gethostname())
