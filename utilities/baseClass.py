import pytest
import os
from ConfigParser import ConfigParser
from utilities.do_request import DoRequest

configParser = ConfigParser()
configParser.read("../configuration/config.ini")


@pytest.mark.usefixtures("setup")
class BaseClass():
    do_request = DoRequest()

    def get_config(self):
        # Read config.ini file
        props = dict(configParser.items(os.environ.get("CONF", "DEFAULT")))
        return props

    def list_users(self):
        url = self.get_config()["getuserslisturl"]
        self.users_list_response = self.do_request.get_expect_200(url, 2)

    def verify_users_list(self):
        count = len(self.users_list_response["data"])
        assert count == 6

    def create_user(self, name, job):
        url = self.get_config()["createuserurl"]
        payload = {"name": name, "job": job}
        self.create_user_response = self.do_request.post_expect_201(url, payload)

    def verify_user_created(self, name, job):
        new_user_id = self.create_user_response["id"]
        new_user_name = self.create_user_response["name"]
        new_user_job = self.create_user_response["job"]
        assert new_user_id != None
        assert new_user_name == name
        assert new_user_job == job
