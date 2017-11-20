from basemodule import BaseModule


class Logos(BaseModule):
    """Module to invoke logos API of VBB REST"""
    def __init__(self, requester=None):
        super(Logos, self).__init__(requester)

    def get_line(self, type=None):
        data, headers = self.r.request('logos/{}'.format(type))

        return data
