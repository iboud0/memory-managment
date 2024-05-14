from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.models.process import Process
from mmu.strategy.memory_allocation_strategy import MemoryAllocationStrategy
class MMU:
    def __init__(self, total_memory_size: int, strategy: MemoryAllocationStrategy, process_table: List[Process], allocation_unit: int = 1):
        self.allocation_unit = allocation_unit
        num_blocks = total_memory_size // allocation_unit
        self.memory_blocks = [MemoryBlock(allocation_unit) for _ in range(num_blocks)]
        self.strategy = strategy
        self.process_table = process_table

    def allocate_memory(self, amount: int, process_id: int) -> int:
        base, limit = self.strategy.allocate_memory(amount, self.memory_blocks)
        print("base:", base, "limit:", limit)
        if base >= 0:
            for process in self.process_table:
                if process.process_id == process_id:
                    process.base = base
                    process.limit = limit
                    return process_id
            return -2
        else:
            return -1

    def free_memory(self, process_id: int) -> bool:
        for process in self.process_table:
            if process.process_id == process_id:
                start_block_idx = process.base
                end_block_idx = process.limit // self.allocation_unit + start_block_idx

                for i in range(start_block_idx, end_block_idx):
                    self.memory_blocks[i].is_free = True
                    
                return True
        raise RuntimeError("Invalid process ID")

    def print_memory_map(self) -> str:
        return "\n".join(str(block) for block in self.memory_blocks)

    def convert_virtual_to_physical(self, process_id: int, virtual_address: int) -> int:
        for process in self.process_table:
            if process.process_id == process_id:
                return process.base + virtual_address - 1
        raise RuntimeError("Invalid process ID or virtual address")
