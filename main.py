from mmu.mmu import MMU
from mmu.strategies.best_fit import BestFitStrategy
from mmu.strategies.first_fit import FirstFitStrategy
from mmu.strategies.next_fit import NextFitStrategy
from mmu.strategies.worst_fit import WorstFitStrategy

def main():
    print("Initializing MMU with 10000KB of memory and Best Fit strategy...")
    mmu = MMU(10000, BestFitStrategy())

    while True:
        command = input("Enter command: ").split()
        if not command:
            continue

        try:
            if command[0] == "cr":
                size = int(command[1])
                pid = mmu.allocate_memory(size)
                print(f"Process created with ID: {pid}")
            elif command[0] == "dl":
                del_pid = int(command[1])
                mmu.free_memory(del_pid)
                print(f"Process {del_pid} deleted.")
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

if __name__ == "__main__":
    main()
