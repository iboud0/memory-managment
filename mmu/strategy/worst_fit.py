import random
from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategy.memory_allocation_strategy import MemoryAllocationStrategy

class WorstFitStrategy(MemoryAllocationStrategy):
    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> int:
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
                        print(index)
                        available_spaces.append((index + 1 - current_space // block_size, current_space))
                    current_space = 0
                else:
                    if current_space >= amount:
                        print(index)
                        available_spaces.append((index - current_space // block_size, current_space))
                    current_space = 0
                    
        if not available_spaces:
            return -1, None # No suitable space found for allocation

        worst_fit = max(available_spaces, key=lambda x: x[1])
        allocated_mem_slots = amount // block_size

        for i in range(allocated_mem_slots):
            memory_blocks[worst_fit[0] + i].is_free = False

        return worst_fit[0], amount