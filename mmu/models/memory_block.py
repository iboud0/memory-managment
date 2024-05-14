class MemoryBlock:
    """
    Represents a block of memory with a specific size and availability status.

    Attributes:
        _size (int): The size of the memory block.
        _is_free (bool): The availability status of the memory block. True indicates the block is free,
            while False indicates it is allocated.
        _process_id (int): The ID of the process that occupies this memory block. Default is -1, indicating
            that the block is not occupied by any process.

    Methods:
        __init__(self, size):
            Initializes a MemoryBlock object with the given size.

        __str__(self):
            Returns a string representation of the MemoryBlock object.
    """

    def __init__(self, size):
        """
        Initializes a MemoryBlock object with the given size.

        Args:
            size (int): The size of the memory block.
        """
        self._size = size
        self._is_free = True
        self._process_id = -1

    @property
    def size(self):
        """
        Get the size of the memory block.

        Returns:
            int: The size of the memory block.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size of the memory block.

        Args:
            value (int): The new size of the memory block.
        """
        self._size = value

    @property
    def is_free(self):
        """
        Get the availability status of the memory block.

        Returns:
            bool: True if the memory block is free, False otherwise.
        """
        return self._is_free

    @is_free.setter
    def is_free(self, value):
        """
        Set the availability status of the memory block.

        Args:
            value (bool): The new availability status of the memory block.
        """
        self._is_free = value
        if value:
            self._process_id = -1

    def __str__(self):
        """
        Returns a string representation of the MemoryBlock object.

        Returns:
            str: A string representation of the MemoryBlock object.
        """
        return f"MemoryBlock{{size={self._size}, is_free={self._is_free}}}"
