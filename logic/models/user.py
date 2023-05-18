import logic.validators.user as validator
from jsonschema import validate
from database.schemas.user import card as collection


def add_user(params: dict) -> bool:
    validate(params, validator.add_user) # if no exception validation passed
    result = collection.insert_one(params)
    return result.inserted_id is not None

def get_users(params: dict) -> list:
    validate(params, validator.get_users) # if no exception validation passed
    result = list(collection.find({}, {'_id': 0}))
    return result

def delete_user(params: dict) -> bool:
    validate(params, validator.delete_user) # if no exception validation passed
    result = collection.delete_one(params)
    return result.deleted_count == 1