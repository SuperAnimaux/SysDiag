import psutil
import time

def recupUsageDisk():
    disk_usage = tuple(psutil.disk_io_counters())
    disk_usage = [(100.0 * disk_usage[i + 1]) / disk_usage[i] for i in range(0, len(disk_usage), 2)]
    disk_usage = (disk_usage[0] + disk_usage[1] + disk_usage[2]) / 3
    return disk_usage

for _ in range(1000000):
    print(recupUsageDisk())
