from base.api_base.baseClass import BaseClass
import logging
import pytest

log = logging.getLogger(__name__)

class TestDeleteUser(BaseClass):

    @pytest.mark.Smoke
    def test_delete_user(self):
        self.delete_user(2)
        self.verify_user_deleted()
        log.debug("test finished")
        pass

    # @pytest.mark.skipif(1>0, reason="Skipping the test based on condition")
    def test_get_single_user(self):
        pass

    # @pytest.mark.skip
    def test_single_user_not_found(self):
        pass