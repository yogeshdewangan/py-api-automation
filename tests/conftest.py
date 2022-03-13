import pytest
import os
import logging
log = logging.getLogger(__name__)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file_path = os.path.join(ROOT_DIR, "inputs\data.csv").replace("tests\\", "")

# @pytest.fixture(scope="class")
# def setup(request):
#     # Read command line parameter and put it in environment variable
#     os.environ['CONF'] = request.config.getoption("testenv", "DEFAULT")
#
#     log.debug("setup")
#     yield
#     log.debug("teardown")


@pytest.fixture(scope="function")
def setup(request):
    print("setup_test called")
    # try:
    #     output_file_path = os.path.join(ROOT_DIR, "outputs\data.csv").replace("tests\\", "")
    #     os.remove(output_file_path)
    # except:
    #     pass


    yield
    print("teardown called")

def pytest_addoption(parser):
    parser.addoption("--testenv", action="store", default="DEFAULT")

@pytest.fixture()
def read_inputfile(self):

    return input