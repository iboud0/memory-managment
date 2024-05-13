class MemoryBlock:
    def __init__(self, size):
        self._size = size
        self._process_id = -1
        self._is_free = True

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
        self._is_free = False if value != -1 else True

    @property
    def is_free(self):
        return self._is_free

    @is_free.setter
    def is_free(self, value):
        self._is_free = value
        if value:
            self._process_id = -1

    def __str__(self):
        return f"MemoryBlock{{process_id={self._process_id}, size={self._size}, is_free={self._is_free}}}"
