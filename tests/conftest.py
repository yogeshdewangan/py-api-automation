import pytest
import os
import logging
log = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def setup(request):
    # Read command line parameter and put it in environment variable
    os.environ['CONF'] = request.config.getoption("testenv", "DEFAULT")

    log.debug("setup")
    yield
    log.debug("teardown")


# @pytest.fixture(scope="function")
# def setup(request):
#     print("setup_test called")
#     yield
#     print("teardown called")

def pytest_addoption(parser):
    parser.addoption("--testenv", action="store", default="DEFAULT")