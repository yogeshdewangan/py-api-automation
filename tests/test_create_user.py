from utilities.baseClass import BaseClass


class TestCreateUsers(BaseClass):

    def test_create_user(self):
        self.create_user("Yogesh", "QA")
        self.verify_user_created("Yogesh", "QA")

    def test_update_user(self):
        pass