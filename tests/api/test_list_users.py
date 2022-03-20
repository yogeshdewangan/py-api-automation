import pytest

from base.api_base.baseClass import BaseClass
import logging

log = logging.getLogger(__name__)

class TestUsers(BaseClass):

    @pytest.mark.Smoke
    def test_list_users(self):
        # self.list_users()
        # self.verify_users_list()
        # log.debug("test finished")
        pass

    def test_get_single_user(self):
        pass

    def test_single_user_not_found(self):
        pass

    def test_get_with_oauth(self):
        self.oauth_test()