import schemas as _schemas

DEBUG = True
INFO = '_info'

MONGO_HOST = 'mongo'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'password'
MONGO_DBNAME = 'data-api'

AUTH_FIELD = 'user_id'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {'offers': _schemas.offers}
