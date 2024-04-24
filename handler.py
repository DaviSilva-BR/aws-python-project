import json


def hello(event, context):
    body = {
        "message": "FOIII!!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
