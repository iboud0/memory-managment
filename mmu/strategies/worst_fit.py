import random
from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategies.memory_allocation_strategy import MemoryAllocationStrategy

class WorstFitStrategy(MemoryAllocationStrategy):
    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> MemoryBlock:
        worst_fit = None
        max_size = 0

        for block in memory_blocks:
            if block.is_free and block.limit >= amount and block.limit > max_size:
                worst_fit = block
                max_size = block.limit

        if worst_fit is not None:
            worst_fit.is_free = False
            worst_fit.set_process_id(random.randint(0, 10000))

        return worst_fit

    def free_memory(self, process_id: int, memory_blocks: List[MemoryBlock]) -> bool:
        for block in memory_blocks:
            if block.process_id == process_id and not block.is_free:
                block.is_free = True
                block.set_process_id(-1)
                return True
        return False
