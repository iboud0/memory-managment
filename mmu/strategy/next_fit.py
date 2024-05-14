import random
from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategy.memory_allocation_strategy import MemoryAllocationStrategy

class NextFitStrategy(MemoryAllocationStrategy):
    def __init__(self):
        self.last_index = 0

    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> MemoryBlock:
        initial_index = self.last_index
        while True:
            block = memory_blocks[self.last_index]
            if block.is_free and block.limit >= amount:
                block.is_free = False
                block.set_process_id(random.randint(0, 10000))
                self.last_index = (self.last_index + 1) % len(memory_blocks)
                return block
            self.last_index = (self.last_index + 1) % len(memory_blocks)
            if self.last_index == initial_index:
                break
        return None

    def free_memory(self, process_id: int, memory_blocks: List[MemoryBlock]) -> bool:
        for block in memory_blocks:
            if block.process_id == process_id and not block.is_free:
                block.is_free = True
                block.set_process_id(-1)
                return True
        return False
