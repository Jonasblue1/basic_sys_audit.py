import platform
import psutil

def system_audit():
    print("System Audit Report")
    print("====================")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"Memory: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")
    print(f"Boot Time: {psutil.boot_time()}")

if __name__ == "__main__":
    system_audit()
