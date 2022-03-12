from base.api_base.baseClass import BaseClass


class TestCreateUsers(BaseClass):

    def test_create_user(self):
        self.update_user("Yogesh", "DevOps", user_id=2)
        self.verify_user_updated("Yogesh", "DevOps")

    def test_update_user(self):
        pass