import pytest

from utilities import xl_utility
from utilities.baseClass import BaseClass


class TestWithMultipleData(BaseClass):

    def test_with_multiple_data(self):
        data_list = xl_utility.get_data_from_xl()
        pass


