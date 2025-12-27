import platform
import psutil

def system_info():
    print("=== SYSTEM INFORMATION ===")
    print(f"OS        : {platform.system()}")
    print(f"Machine   : {platform.machine()}")


def main():
    system_info()
    cpu_check()
    memory_check()
    disk_check()

if __name__ == "__main__":
    main()