import pytest
import os
from configparser import ConfigParser

@pytest.fixture(scope="class")
def setup(request):
    # Read command line parameter
    os.environ['CONF'] = request.config.getoption("testenv")

    print("setup1")
    yield
    print("teardown")

def pytest_addoption(parser):
    parser.addoption("--testenv", action="store", default="DEFAULT")