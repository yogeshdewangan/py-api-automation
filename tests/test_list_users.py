from utilities.baseClass import BaseClass
import logging

log = logging.getLogger(__name__)

class TestUsers(BaseClass):
    def test_list_users(self):
        self.list_users()
        self.verify_users_list()
        log.debug("test finished")
        pass

    def test_get_single_user(self):
        pass

    def test_single_user_not_found(self):
        pass