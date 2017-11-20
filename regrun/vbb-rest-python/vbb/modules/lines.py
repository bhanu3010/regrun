from basemodule import BaseModule


class Lines(BaseModule):
    """Module to invoke lines API of VBB REST"""
    def __init__(self, requester=None):
        super(Lines, self).__init__(requester)

    def get_lines(self, id=None, name=None, operator=None, mode=None, product=None, variants='true'):
        data = self.r.request('lines', payload=locals(), raw=True)

        return data

    def get_line(self, _id=None):
        data, headers = self.r.request('lines/{}'.format(_id))

        return data
