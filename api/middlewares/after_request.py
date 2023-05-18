from flask import current_app as app
from errors.handler import handler


@app.after_request
def after_request(response):
    # print(dir(response))
    print(response.json)
    return response