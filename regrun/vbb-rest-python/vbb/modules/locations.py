from basemodule import BaseModule


class Locations(BaseModule):
    """Module to invoke locations API of VBB REST"""
    def __init__(self, requester=None):
        super(Locations, self).__init__(requester)

    def get_locations(self, query=None, results=10, stations=True, poi=True, addresses=True):
        data, headers = self.r.request('locations', payload=locals())

        return data
