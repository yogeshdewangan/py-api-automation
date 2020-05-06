from utilities.baseClass import BaseClass
import logging

log = logging.getLogger(__name__)

class TestDeleteUser(BaseClass):

    def test_delete_user(self):
        self.delete_user(2)
        self.verify_user_deleted()
        log.debug("test finished")
        pass

    def test_get_single_user(self):
        pass

    def test_single_user_not_found(self):
        pass