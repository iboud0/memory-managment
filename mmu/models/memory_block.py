class MemoryBlock:
    def __init__(self, size):
        self._size = size
        self._is_free = True

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def is_free(self):
        return self._is_free

    @is_free.setter
    def is_free(self, value):
        self._is_free = value
        if value:
            self._process_id = -1

    def __str__(self):
        return f"MemoryBlock{{size={self._size}, is_free={self._is_free}}}"
