from __future__ import print_function
import requests
import requests.packages.urllib3

from .endpoint_manager import EndpointManager
from .exceptions import *

requests.packages.urllib3.disable_warnings()


class Requester(EndpointManager):
    """Base class responsible to trigger requests to VBB rest API"""
    def __init__(self):
        super(Requester, self).__init__()
        self.response = object

    def request(self, endpoint_name=None, endpoint_format=None,
                payload=None, raw=False, raw_url=None, headers=None):
        """request function to initiate call to VBB rest api.

        :param endpoint_name: target endpoint to call the service.
        :param endpoint_format: format of the target endpoint(JSON/YAML etc.)
        :param payload: request payload to pass it to ``requests`` module.
        :param raw: flag to toggle raw data parsing.
        :param raw_url: URL retrieved from composed dict of same class.
        :param headers: intended headers to be passed.

        :returns response: response in json format.

        """

        if payload is None:
            payload = {}

        if endpoint_format:
            raw_url = self[endpoint_name]

            if isinstance(endpoint_format, str):
                url = raw_url.format(endpoint_format)
            else:
                url = raw_url.format(*endpoint_format)
        elif raw_url:
            url = raw_url
        else:
            url = self[endpoint_name]

        self.response = requests.get(url, params=payload, verify=False, headers=headers)
        self.check_for_exceptions(self.response)
        if raw:
            return self.response
        return self.response.json(), self.response.headers

    @staticmethod
    def check_for_exceptions(response):
        """Evaluate for exceptions from response object"""
        status_code = response.status_code
        url = response.url
        if status_code == 200:
            return
        elif status_code == 400:
            raise InvalidInputException("Invalid input")
        elif status_code == 404:
            raise NotFoundException("Not Found")
        else:
            raise ConnectionErrorException("The website couldn't be retrieved, status_code: {}, url: {}".
                                           format(status_code, url))
