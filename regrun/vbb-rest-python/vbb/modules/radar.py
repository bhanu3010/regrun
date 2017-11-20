from basemodule import BaseModule


class Radar(BaseModule):
    """Module to invoke radar API of VBB REST"""
    def __init__(self, requester=None):
        super(Radar, self).__init__(requester)

    def get_radar(self, north=None, west=None, south=None, east=None,
                  results=256, duration=30, frames=3
                  ):
        data, headers = self.r.request('radar', payload=locals())

        return data
