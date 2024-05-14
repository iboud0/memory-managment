from abc import ABC, abstractmethod
from typing import List
from mmu.models.memory_block import MemoryBlock

class MemoryAllocationStrategy(ABC):
    """
    Abstract base class for memory allocation strategies.

    Methods:
        allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> int:
            Abstract method to allocate memory. Must be implemented by subclasses.
    """

    @abstractmethod
    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> int:
        """
        Abstract method to allocate memory. Must be implemented by subclasses.

        Args:
            amount (int): The amount of memory to allocate.
            memory_blocks (List[MemoryBlock]): List of MemoryBlock objects representing available memory blocks.

        Returns:
            int: Index of the allocated memory block. If allocation is unsuccessful, returns -1.
        """
        pass
