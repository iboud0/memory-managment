import random
from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategies.memory_allocation_strategy import MemoryAllocationStrategy

class BestFitStrategy(MemoryAllocationStrategy):
    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> MemoryBlock:
        best_fit = None
        min_size = float('inf')

        for block in memory_blocks:
            if block.is_free and block.limit >= amount and block.limit - amount < min_size:
                best_fit = block
                min_size = block.limit - amount

        if best_fit is not None:
            best_fit.is_free = False
            best_fit.set_process_id(random.randint(0, 10000))

        return best_fit

    def free_memory(self, process_id: int, memory_blocks: List[MemoryBlock]) -> bool:
        for block in memory_blocks:
            if block.process_id == process_id and not block.is_free:
                block.is_free = True
                block.set_process_id(-1)
                return True
        return False
