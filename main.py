import re
import random
from typing import List
from mmu.mmu import MMU
from mmu.models.process import Process
from mmu.strategy.best_fit import BestFitStrategy
from mmu.strategy.first_fit import FirstFitStrategy
from mmu.strategy.next_fit import NextFitStrategy
from mmu.strategy.worst_fit import WorstFitStrategy

def main():
    """
    Main function to run the memory management simulation.
    """
    
    # Initialize memory size and strategy
    mem_size = 4
    strategy = NextFitStrategy()  # Change the strategy here if needed

    # Initialize process table and MMU
    process_table: List[Process] = []
    mmu = MMU(mem_size, strategy, process_table)
    print(f"Initializing MMU with {mem_size}KB of memory and {format_class_name(strategy.__class__.__name__)}...")

    while True:
        # Read user command
        command = input("> ").split()
        if not command:
            continue

        try:
            # Process user commands
            if command[0] == "cr":  # Create process
                size = int(command[1])
                pid = generate_unique_pid(process_table)
                process_table.append(Process(pid))
                pid_ = mmu.allocate_memory(size, pid)
                if pid_ != -1 and pid_ != -2:
                    print(f"Process created with ID: {pid}")
                elif pid_ == -1:
                    print(f"No available space")
                else:
                    print("Error within process")
            elif command[0] == "dl":  # Delete process
                del_pid = int(command[1])
                mmu.free_memory(del_pid)
                del_index = next((i for i, process in enumerate(process_table) if process.process_id == del_pid), None)
                if del_index is not None:
                    del process_table[del_index]
                    print(f"Process {del_pid} deleted.")
                else:
                    print(f"Process with ID {del_pid} not found.")
            elif command[0] == "pm":  # Print memory map
                print(mmu.print_memory_map())
            elif command[0] == "cv":  # Convert virtual address to physical address
                cv_pid = int(command[1])
                virtual_address = int(command[2])
                physical_address = mmu.convert_virtual_to_physical(cv_pid, virtual_address)
                print(f"Physical Address: {physical_address}")
            elif command[0] == "exit":  # Exit the program
                return
            else:
                print("Unknown command.")
        except Exception as e:
            print(f"Error: {e}")

def generate_unique_pid(process_table: List[Process]) -> int:
    """
    Generates a unique process ID that is not already present in the process table.

    Args:
        process_table (List[Process]): The list of existing processes.

    Returns:
        int: A unique process ID.
    """
    while True:
        pid = random.randint(1, 10000)
        if pid not in [process.process_id for process in process_table]:
            return pid
        
def format_class_name(class_name):
        """
        Formats a class name into a readable string by separating words with spaces.
        
        Args:
            class_name (str): The class name to format.
        
        Returns:
            str: The formatted class name.
        """
        return ' '.join(word.lower() for word in re.findall('[A-Z][a-z]*', class_name))
        
if __name__ == "__main__":
    main()
