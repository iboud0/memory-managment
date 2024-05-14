import math
from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategy.memory_allocation_strategy import MemoryAllocationStrategy

class BestFitStrategy(MemoryAllocationStrategy):
    """
    A memory allocation strategy that allocates memory using the Best Fit algorithm.

    Attributes:
        None

    Methods:
        allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> int:
            Allocates memory using the Best Fit algorithm.

    """

    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> int:
        """
        Allocates memory using the Best Fit algorithm.

        Args:
            amount (int): The amount of memory to allocate.
            memory_blocks (List[MemoryBlock]): List of MemoryBlock objects representing available memory blocks.

        Returns:
            Tuple[int, int]: A tuple containing the index of the allocated memory block and the allocated memory size.
                             If no suitable space is found for allocation, returns (-1, None).
        """
        available_spaces = []
        current_space = 0
        block_size = memory_blocks[0].size

        # Look for available spaces in memory
        for index, block in enumerate(memory_blocks):
            if block.is_free:
                current_space += block.size
            if not block.is_free or block == memory_blocks[-1]:
                if block == memory_blocks[-1]:
                    if current_space >= amount:
                        available_spaces.append((index + 1 - current_space // block_size, current_space))
                    current_space = 0
                else:
                    if current_space >= amount:
                        available_spaces.append((index - current_space // block_size, current_space))
                    current_space = 0
                    
        if not available_spaces:
            return -1, None # No suitable space found for allocation

        best_fit = min(available_spaces, key=lambda x: x[1])
        allocated_mem_slots = math.ceil(amount / block_size)

        # Mark allocated memory slots as occupied
        for i in range(allocated_mem_slots):
            memory_blocks[best_fit[0] + i].is_free = False

        return best_fit[0], amount
