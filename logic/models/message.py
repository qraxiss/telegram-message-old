import logic.validators.message as validator
from jsonschema import validate
from config import BOT

from logic.models.user import get_users
from concurrent.futures import ThreadPoolExecutor


def send_msg(params: dict) -> bool:
    validate(params, validator.send_msg)  # if no exception validation passed

    users = get_users({})

    with ThreadPoolExecutor() as executor:

        futures = {
            user['userId'] : executor.submit(
                BOT.send_message, user['userId'], params['text']
            )
            for user in users
        }

        return {
           user: future.result().message_id for user, future in futures.items()
        }

    return [message.result().message_id for message in messages]
