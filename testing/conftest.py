import pytest

from conftest_wrapper import wrapper_client

@pytest.fixture(scope="module")
def client(request):
    return wrapper_client("dev")
 