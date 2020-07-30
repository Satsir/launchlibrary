import pytest
import os
import shutil
from launchlibrary.main.local_files.local_files import LocalFiles
from launchlibrary.main.api.api import API
from launchlibrary.main.local_files.constants import REQ_RES_DIR


@pytest.fixture(autouse=True)
def making_req_res_dir():
    A1 = API()
    LF1 = LocalFiles()
    A1.get_launches(2021, 2023)
    LF1.store_request_results(A1)
    yield
    shutil.rmtree(REQ_RES_DIR, ignore_errors=True)


def test_store_request_results():
    if os.path.exists(REQ_RES_DIR):
        assert True, "Directory was not made."
    else:
        assert False

def test_clear_all_request_results():
    A1 = API()
    LF1 = LocalFiles()
    A1.get_launches(2021, 2023)
    LF1.store_request_results(A1)
    if os.path.exists(REQ_RES_DIR):
        LF1.clear_all_request_results()
        if not os.path.exists(REQ_RES_DIR):
            assert True, "Clear was not successful."
        else:
            assert False


