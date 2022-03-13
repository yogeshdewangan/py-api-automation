import pytest

from base.api_base.baseClass import BaseClass


class TestCreateUsers(BaseClass):

    @pytest.mark.Smoke
    def test_create_user(self):
        self.create_user("Yogesh", "QA")

        self.verify_user_created("Yogesh", "QA")


    @pytest.mark.Sanity
    def test_update_user(self):
        pass




