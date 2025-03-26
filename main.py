import click
from RecupCharge.chargecpu import recupUsageCPU
from RecupCharge.chargeram import recupUsageRAM
from RecupCharge.usageDisk import recupUsageDisk



def main():
    print("Bienvenue")

    while True:
        print("---------Commandes-------------")
        print("Charge CPU : chargeCPU")
        print("Charge RAM: chargeRAM")
        print("Disk Usage : diskUsage")
        print("Arret : 0")

        command = input("-------Entrez votre commande------\n>> ").strip()

        if command == "chargeCPU":
            charge(True)
        elif command == "chargeRAM":
            charge(False, True)
        elif command == "diskUsage":
            usage(True)
        elif command == "0":
            break



def charge(cpu=False, ram=False):
    if cpu:
        try:
            chargeCPU = recupUsageCPU()
            print(f"La charge CPU est de : {chargeCPU}%")

        except Exception as e:
            print(f"Une erreur est survenue, veuillez essayer dans quelques instants. {e}")

    if ram:
        try:
            chargeRAM = recupUsageRAM()
            print(f"La charge RAM est de : {chargeRAM}%")
        except Exception as e:
            print(f"Une erreur est survenue, veuillez essayer dans quelques instants. {e}")



def usage(disk=False):
    if disk:
        try:
            usageDisk = recupUsageDisk()
            print(f"L'usage du disque dur est de : {usageDisk}%")
        except Exception as e:
            print(f"Une erreur est survenue, veuillez essayer dans quelques instants. {e}")



if __name__ == '__main__':
    main()