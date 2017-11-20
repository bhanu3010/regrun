from basemodule import BaseModule


class Stations(BaseModule):
    """Module to invoke stations API of VBB REST"""
    def __init__(self, requester=None):
        super(Stations, self).__init__(requester)

    def query_stations(self, query=None, completion=True, fuzzy=False):
        data, headers = self.r.request('stations', payload=locals())

        return data

    def get_station(self, id=None, name=None, latitude=None, longitude=None, weight=None):
        data, headers = self.r.request('stations', payload=locals())

        return data

    def get_all_stations(self):
        data, headers = self.r.request('stations/all')

        return data

    def get_nearby_stations(self, latitude=None, longitude=None, results=8,
                            distance=None, stations='true', poi='false'):
        data, headers = self.r.request('stations/nearby', payload=locals())

        return data

    def get_station_by_id(self, id=None):
        data, headers = self.r.request('stations/{}'.format(id))

        return data

    def get_station_departures(self, id=None, when=None, results=10, maxQueries=10, nextStation=None):
        data, headers = self.r.request('stations/{}/departures'.format(id), payload=locals())

        return data
