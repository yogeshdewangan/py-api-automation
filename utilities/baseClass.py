import pytest
import requests

from configuration import getconfig



@pytest.mark.usefixtures("setup")
class BaseClass():

    def list_users(self):
        url = getconfig.props["getuserslisturl"]
        self.content = requests.get(url).json()

    def verify_users_list(self):
        count = len(self.content["data"])
        assert count == 6
        pass
