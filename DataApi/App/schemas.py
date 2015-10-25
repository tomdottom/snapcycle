offer_schema = {
    'title': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
    'description': {
        'type': 'string',
        'minlength': 25,
        'maxlength': 999,
        'required': True,
    }
}

offers = {
    'item_title': 'offer',
    'schema': offer_schema,
    'public_methods': ['GET', 'POST'],
    'public_item_methods': ['GET'],
}
