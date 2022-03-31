
import json
from masonite.utils.collections import collect

def res(data, message='', status=200, response=None):
    # dd(data)
    if response:
        response.status(status)
    # dd(data, typeof(data))
    return {
        "message": message,
        "code": status,
        "data": data
    }

def resModel(data, message='', status=200, response=None):
    return res(json.loads(data.to_json()), message, status, response)

def resJson(data, message='', status=200, response=None):
    return res(json.loads(data), message, status, response)

def typeof(variate):
    type = None
    if isinstance(variate, int):
        type = "int"
    elif isinstance(variate, str):
        type = "str"
    elif isinstance(variate, float):
        type = "float"
    elif isinstance(variate, list):
        type = "collect"
    elif isinstance(variate, tuple):
        type = "tuple"
    elif isinstance(variate, dict):
        type = "dict"
    elif isinstance(variate, set):
        type = "set"
    elif isinstance(variate, collect):
        type = "collect"
    return type
