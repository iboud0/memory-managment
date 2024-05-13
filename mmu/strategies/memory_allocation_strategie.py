from abc import ABC, abstractmethod
from typing import List
from mmu.models.memory_block import MemoryBlock

class MemoryAllocationStrategy(ABC):
    @abstractmethod
    def allocate_memory(self, amount: int, memory_blocks: List[MemoryBlock]) -> MemoryBlock:
        pass

    @abstractmethod
    def free_memory(self, process_id: int, memory_blocks: List[MemoryBlock]) -> bool:
        pass
