import psutil


def recupUsageDisk():
    disk_usage = psutil.disk_usage('/').percent
    return disk_usage

