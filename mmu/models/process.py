class Process:
    def __init__(self, process_id, base, limit):
        self._process_id = process_id
        self._base = base
        self._limit = limit

    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
