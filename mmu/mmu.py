from typing import List
from mmu.models.memory_block import MemoryBlock
from mmu.models.process import Process
from mmu.strategy.memory_allocation_strategy import MemoryAllocationStrategy

class MMU:
    """
    Memory Management Unit (MMU) class responsible for memory allocation and management.

    Attributes:
        allocation_unit (int): The size of each memory allocation unit.
        memory_blocks (List[MemoryBlock]): List of MemoryBlock objects representing available memory blocks.
        strategy (MemoryAllocationStrategy): The memory allocation strategy to be used.
        process_table (List[Process]): List of Process objects representing active processes.

    Methods:
        __init__(self, total_memory_size: int, strategy: MemoryAllocationStrategy, process_table: List[Process], allocation_unit: int = 1):
            Initializes the MMU with the specified parameters.

        allocate_memory(self, amount: int, process_id: int) -> int:
            Allocates memory for a process based on the specified amount and process ID.

        free_memory(self, process_id: int) -> bool:
            Frees memory allocated to a process based on its process ID.

        print_memory_map(self) -> str:
            Generates a string representation of the current memory map.

        convert_virtual_to_physical(self, process_id: int, virtual_address: int) -> int:
            Converts a virtual address to its corresponding physical address for a given process.
    """

    def __init__(self, total_memory_size: int, strategy: MemoryAllocationStrategy, process_table: List[Process], allocation_unit: int = 1):
        """
        Initializes the MMU with the specified parameters.

        Args:
            total_memory_size (int): Total size of memory.
            strategy (MemoryAllocationStrategy): The memory allocation strategy to be used.
            process_table (List[Process]): List of Process objects representing active processes.
            allocation_unit (int, optional): The size of each memory allocation unit. Defaults to 1.
        """
        self.allocation_unit = allocation_unit
        num_blocks = total_memory_size // allocation_unit
        self.memory_blocks = [MemoryBlock(allocation_unit) for _ in range(num_blocks)]
        self.strategy = strategy
        self.process_table = process_table

    def allocate_memory(self, amount: int, process_id: int) -> int:
        """
        Allocates memory for a process based on the specified amount and process ID.

        Args:
            amount (int): The amount of memory to allocate.
            process_id (int): The ID of the process.

        Returns:
            int: Process ID if memory allocation is successful, -1 if no suitable space found, -2 if process ID is invalid.
        """
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
        """
        Frees memory allocated to a process based on its process ID.

        Args:
            process_id (int): The ID of the process.

        Returns:
            bool: True if memory is successfully freed, False otherwise.
        """
        for process in self.process_table:
            if process.process_id == process_id:
                start_block_idx = process.base
                end_block_idx = process.limit // self.allocation_unit + start_block_idx

                for i in range(start_block_idx, end_block_idx):
                    self.memory_blocks[i].is_free = True
                    
                return True
        raise RuntimeError("Invalid process ID")

    def print_memory_map(self) -> str:
        """
        Generates a string representation of the current memory map.

        Returns:
            str: String representation of the current memory map.
        """
        # TODO: re-implement properly
        return "\n".join(str(block) for block in self.memory_blocks)

    def convert_virtual_to_physical(self, process_id: int, virtual_address: int) -> int:
        """
        Converts a virtual address to its corresponding physical address for a given process.

        Args:
            process_id (int): The ID of the process.
            virtual_address (int): The virtual address to be converted.

        Returns:
            int: The corresponding physical address.
        """
        for process in self.process_table:
            if process.process_id == process_id:
                return process.base + virtual_address - 1
        raise RuntimeError("Invalid process ID or virtual address")
