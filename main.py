import random
from typing import List
from mmu.mmu import MMU
from mmu.models.process import Process
from mmu.strategy.best_fit import BestFitStrategy
from mmu.strategy.first_fit import FirstFitStrategy
from mmu.strategy.next_fit import NextFitStrategy
from mmu.strategy.worst_fit import WorstFitStrategy

def main():
    print("Initializing MMU with 10000KB of memory and Best Fit strategy...")
    process_table: List[Process] = []
    mmu = MMU(10000, BestFitStrategy(), process_table)

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
