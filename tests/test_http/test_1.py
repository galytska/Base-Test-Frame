import requests

from tests.base_test import BaseTest


class Test1(BaseTest):
    def test_status_code(self):
        r = requests.get('http://httpbin.org/get')
        assert r.status_code == 200, 'Not expected response status code received'
