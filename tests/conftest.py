import pytest
import os
import logging
import utilities.send_email as emailto
from configuration.getconfig import props
log = logging.getLogger(__name__)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file_path = os.path.join(ROOT_DIR, "inputs\data.csv").replace("tests\\", "")


@pytest.fixture(scope="function")
def setup(request):
    print("setup_test called")
    try:
        output_file_path = os.path.join(ROOT_DIR, "outputs\data.csv").replace("tests\\", "")
        os.remove(output_file_path)
    except:
        pass
    yield

    print("teardown called")

def pytest_addoption(parser):
    parser.addoption("--testenv", action="store", default="DEFAULT")

def pytest_sessionfinish(session, exitstatus):
    receiver_emails =  props["receiver_emails"]
    sender_email = props["sender_email"]
    sender_password = props["sender_password"]
    subject = "Html report of pytest pipeline"
    body = subject
    emailto.send_report(subject, body, sender_email, sender_password, receiver_emails  )