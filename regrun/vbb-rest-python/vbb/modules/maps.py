from basemodule import BaseModule


class Maps(BaseModule):
    """Module to invoke maps API of VBB REST"""
    def __init__(self, requester=None):
        super(Maps, self).__init__(requester)

    def get_maps(self, type=None):
        headers = {'content-type': 'application/pdf'}
        data, headers = self.r.request('maps/{}'.format(type), headers=headers)

        return data
