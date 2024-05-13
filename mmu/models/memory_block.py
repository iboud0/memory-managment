class MemoryBlock:
    def __init__(self, base, limit):
        self.base = base
        self.limit = limit
        self.process_id = -1
        self.is_free = True

    def set_process_id(self, process_id):
        self.process_id = process_id
        self.is_free = False if process_id != -1 else True

    def __str__(self):
        return f"MemoryBlock{{process_id={self.process_id}, base={self.base}, limit={self.limit}, is_free={self.is_free}}}"
