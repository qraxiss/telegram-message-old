from helpers.required import required
from database.schemas.user import schema

send_msg = required(
    schema,
    {'text': {'type': 'string'}}
)