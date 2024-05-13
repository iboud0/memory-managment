import random
from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategies.memory_allocation_strategy import MemoryAllocationStrategy

class FirstFitStrategy(MemoryAllocationStrategy):
    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> MemoryBlock:
        for block in memory_blocks:
            if block.is_free and block.limit >= amount:
                block.is_free = False
                block.set_process_id(random.randint(0, 10000))
                return block
        return None

    def free_memory(self, process_id: int, memory_blocks: List[MemoryBlock]) -> bool:
        for block in memory_blocks:
            if block.process_id == process_id:
                block.is_free = True
                block.set_process_id(-1)
                return True
        return False
