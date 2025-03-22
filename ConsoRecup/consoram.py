import psutil


def recupUsageRAM():
    ram_usage = psutil.virtual_memory().percent
    return ram_usage

def estimerConsoRAM(usage_ram, tdp, nbr_barette):
    consoRAM = ((usage_ram/100) * tdp) * nbr_barette
    return consoRAM
for i in range(100):
    print(estimerConsoRAM(recupUsageRAM(), 5, 2))