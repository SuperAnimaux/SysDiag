import psutil



def recupUsageCPU():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def estimerConsoCPU(cpu_usage, tdp):
    conso = (cpu_usage/100) * tdp
    return conso
