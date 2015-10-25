# -*- coding: utf-8 -*-

from eve.auth import TokenAuth
from flask import request, abort, Response
import hmac
import json


SECRET_KEY = "FooBar"


class NotAuthenticatedException(Exception):
    status_code = 401

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class BearerAuth(TokenAuth):
    def __init__(self):
        super(BearerAuth, self).__init__()

    def check_auth(self, token, allowed_roles, resource, method):
        print "check_auth"
        # token is base64 and msgpack encoded object
        if token is None:
            return False
        msg = json.loads(token.decode('base64'))
        shash = msg.pop('shash')
        if hmac.new(SECRET_KEY, json.dumps(msg)) != shash:
            return False
        # Enable resource checking
        # if msg.get('id'):
        #     self.set_request_auth_value(msg[id])
        #     return True
        # return False
        return True

    def authenticate(self):
        print "authenticate"
        raise NotAuthenticatedException("Please login")

    def authorized(self, allowed_roles, resource, method):
        print "authorized"
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            token = None
        return self.check_auth(token, allowed_roles, resource, method)
