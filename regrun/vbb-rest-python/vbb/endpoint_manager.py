from __future__ import unicode_literals


class EndpointManager(object):
    def __init__(self):
        """Endpoint initializer"""
        self.base_url = "https://vbb.transport.rest"

    def __getitem__(self, endpoint):
        """Magical getitem function, used to retrieve URLs"""
        uri = None
        if endpoint.startswith('/'):
            uri = self.base_url + endpoint
        else:
            uri = "/".join([self.base_url, endpoint])
        return uri

