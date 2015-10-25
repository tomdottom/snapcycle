from eve import Eve
from flask import session, url_for, redirect, flash, request, jsonify
from flask_oauthlib.client import OAuth
from auth import BearerAuth, NotAuthenticatedException

app = Eve(auth=BearerAuth)


@app.errorhandler(NotAuthenticatedException)
def handle_not_authenticated(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


oauth = OAuth()
twitter = oauth.remote_app(
    'twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key='<your key here>',
    consumer_secret='<your secret here>'
)


@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')


# @app.route('/login')
# @app.errorhandler(403)
# def login(foo):
#     return twitter.authorize(
#         callback=url_for(
#             'oauth_authorized',
#             next=request.args.get('next') or request.referrer or None
#         )
#     )


@app.route('/oauth-authorized')
def oauth_authorized():
    next_url = request.args.get('next') or url_for('index')
    resp = twitter.authorized_response()
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']

    flash('You were signed in as %s' % resp['screen_name'])
    return redirect(next_url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
