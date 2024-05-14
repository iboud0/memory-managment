import random
from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategy.memory_allocation_strategy import MemoryAllocationStrategy

class FirstFitStrategy(MemoryAllocationStrategy):
    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> int:
        available_space = ()
        current_space = 0
        block_size = memory_blocks[0].size

        # Look for the first available space in memory
        for index, block in enumerate(memory_blocks):
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

        first_fit = available_space
        allocated_mem_slots = amount // block_size

        for i in range(allocated_mem_slots):
            memory_blocks[first_fit[0] + i].is_free = False

        return first_fit[0], amount