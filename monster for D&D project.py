class monsters(object):
    def __init__(self, name, cr):
        self.name = name
        self.cr = cr

    @property
    def name(self):
        return self._name
    @name.setter
    def name (self, value):
        self._name = value
    @property
    def cr(self):
        return self._cr
    @cr.setter
    def cr(self, value):
        self._cr = value
