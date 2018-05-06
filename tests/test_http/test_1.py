import requests

from tests.base_test import BaseTest


class TestResponseStatus(BaseTest):
    def test_response_status_code(self, http_test_url, ref, tst_path):
        r = requests.get(http_test_url + tst_path)
        assert r.status_code == 200, \
            'Not expected response status code received for page "{}"'.format(ref)


