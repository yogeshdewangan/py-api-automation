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


    def test_notepad(self):
        pass
        # read input from csv file

        # open notepad and write the input to notepad

        # Save the file in txt format

        # ready from input == read from txt file will compate with input file for respective test


