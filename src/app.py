# Health Check Endpoints
# '/api/v1/details'
# '/api/v1/healthz'
#
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import request, jsonify
import datetime
import socket


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/api/v1/details')
# ‘/api/v1/details’ URL is bound with details() function.
def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/healthz')
# ‘/api/v1/healthz URL is bound with health() function.
def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
