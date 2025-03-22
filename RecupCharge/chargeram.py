import psutil


def recupUsageRAM():
    ram_usage = psutil.virtual_memory().percent
    return ram_usage