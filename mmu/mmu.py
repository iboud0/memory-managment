from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.strategies.memory_allocation_strategy import MemoryAllocationStrategy

class MMU:
    def __init__(self, total_memory_size: int, strategy: MemoryAllocationStrategy):
        self.memory_blocks = [MemoryBlock(0, total_memory_size)]
        self.strategy = strategy

    def allocate_memory(self, amount: int) -> int:
        allocated_block = self.strategy.allocate_memory(amount, self.memory_blocks)
        if allocated_block:
            allocated_block.is_free = False
            return allocated_block.process_id
        else:
            return -1

    def free_memory(self, process_id: int) -> bool:
        return self.strategy.free_memory(process_id, self.memory_blocks)

    def print_memory_map(self) -> str:
        return "\n".join(str(block) for block in self.memory_blocks)

    def convert_virtual_to_physical(self, process_id: int, virtual_address: int) -> int:
        for block in self.memory_blocks:
            if block.process_id == process_id and not block.is_free and virtual_address < block.limit:
                return block.base + virtual_address
        raise RuntimeError("Invalid process ID or virtual address")
