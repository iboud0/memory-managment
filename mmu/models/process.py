class Process:
    """
    Represents a process in a memory management system.

    Attributes:
        _process_id (int): The ID of the process.
        _base (int): The base address of the process in memory. Default is -1, indicating the process is not loaded.
        _limit (int): The upper limit address of the process in memory. Default is -1, indicating the process is not loaded.

    Methods:
        __init__(self, process_id):
            Initializes a Process object with the given process ID.

    Properties:
        process_id:
            Get or set the ID of the process.

        base:
            Get or set the base address of the process in memory.

        limit:
            Get or set the upper limit address of the process in memory.
    """

    def __init__(self, process_id):
        """
        Initializes a Process object with the given process ID.

        Args:
            process_id (int): The ID of the process.
        """
        self._process_id = process_id
        self._base = -1
        self._limit = -1

    @property
    def process_id(self):
        """
        Get or set the ID of the process.

        Returns:
            int: The ID of the process.
        """
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        """
        Set the ID of the process.

        Args:
            value (int): The new ID of the process.
        """
        self._process_id = value

    @property
    def base(self):
        """
        Get or set the base address of the process in memory.

        Returns:
            int: The base address of the process.
        """
        return self._base

    @base.setter
    def base(self, value):
        """
        Set the base address of the process in memory.

        Args:
            value (int): The new base address of the process.
        """
        self._base = value

    @property
    def limit(self):
        """
        Get or set the upper limit address of the process in memory.

        Returns:
            int: The upper limit address of the process.
        """
        return self._limit

    @limit.setter
    def limit(self, value):
        """
        Set the upper limit address of the process in memory.

        Args:
            value (int): The new upper limit address of the process.
        """
        self._limit = value
