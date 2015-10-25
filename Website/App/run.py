from functools import wraps

from flask import Flask, render_template, redirect, url_for, abort
import json
import requests

app = Flask(__name__)

API_HOST = '192.168.99.100'
API_PORT = '5000'
API = {
    'offers': "http://{}:{}/offers/".format(API_HOST, API_PORT),
    'offer': "http://{}:{}/offers/{}".format(API_HOST, API_PORT, '{offer_id}')
}


def get_api_data(api_endpoint):
    def fdec(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            r = requests.get(api_endpoint.format(**kwargs))
            data = json.loads(r.content)
            return f(data=data)
        return decorated
    return fdec


def handle_api_errors():
    def fdec(f):
        @wraps(f)
        def decorated(data):
            if data.get('_status') == 'ERR':
                abort(int(data.get('_error', {}).get('code') or 404))
            return f(data)
        return decorated
    return fdec


@app.route("/")
def hello():
    return redirect(url_for('offers'), code=302)


@app.route("/offers/<offer_id>/")
@get_api_data(API['offer'])
@handle_api_errors()
def offer(data):
    return render_template('offer.html', data=data)


@app.route("/offers/")
@get_api_data(API['offers'])
@handle_api_errors()
def offers(data):
    return render_template('offers.html', data=data)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
