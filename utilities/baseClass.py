from ConfigParser import ConfigParser

import pytest
import requests
import os
from configuration import getconfig

configParser = ConfigParser()
configParser.read("../configuration/config.ini")

@pytest.mark.usefixtures("setup")
class BaseClass():

    def get_config(self):
        # Read config.ini file
        props = dict(configParser.items(os.environ.get("CONF", "DEFAULT")))
        return props

    def list_users(self):
        url = self.get_config()["getuserslisturl"]
        self.content = requests.get(url).json()

    def verify_users_list(self):
        count = len(self.content["data"])
        assert count == 6
        pass
