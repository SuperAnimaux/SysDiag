import psutil

def get_disk_info():

    partitions = psutil.disk_partitions()

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"--------------------\nPartition: {partition.device}\nMountpoint: {partition.mountpoint}\nFile system type: {partition.fstype}\nTotal: {usage.total / (1024 ** 3):.2f} GB\nUsed: {usage.used / (1024 ** 3):.2f} GB\nFree: {usage.free / (1024 ** 3):.2f} GB\nPercentage used: {usage.percent}%")

        io_counters = psutil.disk_io_counters()
        print(f"\nRead count: {io_counters.read_count}\nWrite count: {io_counters.write_count}\nRead bytes: {io_counters.read_bytes / (1024 ** 3):.2f} GB\nWrite bytes: {io_counters.write_bytes / (1024 ** 3):.2f} GB\nRead time: {io_counters.read_time} ms\nWrite time: {io_counters.write_time} ms\n--------------------")
