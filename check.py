import platform
import psutil

def system_info():
    print("=== SYSTEM INFORMATION ===")
    print(f"OS        : {platform.system()}")
    print(f"Machine   : {platform.machine()}")

def cpu_check():
    usage = psutil.cpu_percent(interval=1)
    print("\n=== CPU STATUS ===")
    print(f"CPU Usage : {usage}%")
    if usage > 80:
        print("WARNING: High CPU usage!")

def memory_check():
    mem = psutil.virtual_memory()
    print("\n=== MEMORY STATUS ===")
    print(f"Usage     : {mem.percent}%")
    if mem.percent > 75:
        print("WARNING: High memory usage!")

def disk_check():
    disk = psutil.disk_usage('/')
    print("\n=== DISK STATUS ===")
    print(f"Usage     : {disk.percent}%")
    if disk.percent > 85:
        print("WARNING: Disk almost full!")

def main():
    system_info()
    cpu_check()
    memory_check()
    disk_check()

if __name__ == "__main__":
    main()
