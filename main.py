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
    def format_class_name(class_name):
        return ' '.join(word.lower() for word in re.findall('[A-Z][a-z]*', class_name))
    
    mem_size = 20
    strategy = NextFitStrategy()
    process_table: List[Process] = []
    mmu = MMU(mem_size, strategy, process_table)
    print(f"Initializing MMU with {mem_size}KB of memory and {format_class_name(strategy.__class__.__name__)}...")
    
    while True:
        command = input("> ").split()
        if not command:
            continue

        try:
            if command[0] == "cr":
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
            elif command[0] == "dl":
                del_pid = int(command[1])
                mmu.free_memory(del_pid)
                del_index = next((i for i, process in enumerate(process_table) if process.process_id == del_pid), None)
                if del_index is not None:
                    del process_table[del_index]
                    print(f"Process {del_pid} deleted.")
                else:
                    print(f"Process with ID {del_pid} not found.")
            elif command[0] == "pm":
                print(mmu.print_memory_map())
            elif command[0] == "cv":
                cv_pid = int(command[1])
                virtual_address = int(command[2])
                physical_address = mmu.convert_virtual_to_physical(cv_pid, virtual_address)
                print(f"Physical Address: {physical_address}")
            elif command[0] == "exit":
                return
            else:
                print("Unknown command.")
        except Exception as e:
            print(f"Error: {e}")

def generate_unique_pid(process_table: List[Process]) -> int:
    while True:
        pid = random.randint(1, 10000)
        if pid not in [process.process_id for process in process_table]:
            return pid
        
if __name__ == "__main__":
    main()
