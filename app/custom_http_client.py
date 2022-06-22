import requests
from requests import Response
from webdriver_manager.core.http import HttpClient


class CustomHttpClient(HttpClient):

    def get(self, url, params=None, **kwargs) -> Response:
        """
        Add you own logic here like session or proxy etc.
        """

        # proxies = {
        #     'http': '',
        #     'https': ''
        # }
        # return requests.get(url, params, proxies=proxies, **kwargs)
        return requests.get(url, params, **kwargs)
