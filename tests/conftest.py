import pytest


@pytest.fixture(scope="class")
def setup(request):
    print("setup1")
    yield
    print("teardown")

