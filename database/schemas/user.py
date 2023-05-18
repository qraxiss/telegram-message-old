from database.schemas.schema import Schema

schema = {
    "type": "object",
    "properties": {
        "userId": {'type': 'number'},
    }
}

card = Schema('users', schema)