from helpers.required import required
from database.schemas.user import schema

add_user = required(
    schema,
    {'userId': {'type': 'number'}}
)

get_users = required(
    schema,
    {}
)

delete_user = required(
    schema,
    {'userId': {'type': 'number'}}
)
