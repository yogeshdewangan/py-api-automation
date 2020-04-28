import json


class JSONParser:
    def __init__(self, data):
        self.__dict__ = json.loads(data)    # json loads will load from json string


