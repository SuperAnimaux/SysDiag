import psutil

def recupUsageCPU():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

