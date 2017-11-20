from basemodule import BaseModule


class Journeys(BaseModule):
    """Module to invoke journeys API of VBB REST"""
    def __init__(self, requester=None):
        super(Journeys, self).__init__(requester)

    def get_journeys(self, _from=None, _to=None, when=None, results=5,
                     via=None, passedStations='false', transfers=5, transferTime=0,
                     accessibility=None, bike='false', suburban='true', subway='true',
                     tram='true', bus='true', ferry='true', express='true', regional='true'):
        params = locals()

        params['from'] = params['_from']
        params['to'] = params['_to']
        del (params['_from'], params['_to'])

        data, headers = self.r.request('journeys', payload=params)

        return data
