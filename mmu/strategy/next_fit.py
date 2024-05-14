from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategy.memory_allocation_strategy import MemoryAllocationStrategy

class NextFitStrategy(MemoryAllocationStrategy):
    """
    A memory allocation strategy that allocates memory using the Next Fit algorithm.

    Attributes:
        next (int): The index to start searching for available memory in the next iteration.

    Methods:
        __init__(self):
            Initializes a NextFitStrategy object.

        allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> int:
            Allocates memory using the Next Fit algorithm.

    """

    def __init__(self):
        """
        Initializes a NextFitStrategy object.

        Args:
            None
        """
        self.next = 0

    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> int:
        """
        Allocates memory using the Next Fit algorithm.

        Args:
            amount (int): The amount of memory to allocate.
            memory_blocks (List[MemoryBlock]): List of MemoryBlock objects representing available memory blocks.

        Returns:
            Tuple[int, int]: A tuple containing the index of the allocated memory block and the allocated memory size.
                             If no suitable space is found for allocation, returns (-1, None).
        """
        available_space = ()
        current_space = 0
        block_size = memory_blocks[0].size

        # Look for the first available space in memory starting from where we stopped in the previous iteration
        for index, block in enumerate(memory_blocks[self.next : ]):
            if block.is_free:
                current_space += block.size
            if not block.is_free or block == memory_blocks[-1]:
                if block == memory_blocks[-1]:
                    if current_space >= amount:
                        available_space = (index + self.next + 1 - current_space // block_size, current_space)
                else:
                    if current_space >= amount:
                        available_space = (index + self.next - current_space // block_size, current_space)
                        break
        
        if not available_space:
            current_space = 0
            if self.next != 0:
                # Start searching from the beginning of memory if no suitable space found from the current position
                for index, block in enumerate(memory_blocks[ : ]):
                    if block.is_free:
                        current_space += block.size
                    if not block.is_free or block == memory_blocks[-1]:
                        if block == memory_blocks[-1]:
                            if current_space >= amount:
                                available_space = (index + 1 - current_space // block_size, current_space)
                        else:
                            if current_space >= amount:
                                available_space = (index - current_space // block_size, current_space)
                                break
                if not available_space:
                    return -1, None # No suitable space found for allocation
            else:
                return -1, None # No suitable space found for allocation

        next_fit = available_space
        allocated_mem_slots = amount // block_size
        # Update the starting index for the next iteration
        if (next_fit[0] + allocated_mem_slots == len(memory_blocks)):
            self.next = 0
        else:
            self.next = next_fit[0] + allocated_mem_slots

        # Mark allocated memory slots as occupied
        for i in range(allocated_mem_slots):
            memory_blocks[next_fit[0] + i].is_free = False

        return next_fit[0], amount
