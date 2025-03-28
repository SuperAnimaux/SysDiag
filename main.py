from RecupCharge.chargecpu import recupUsageCPU
from RecupCharge.chargeram import recupUsageRAM
from RecupCharge.usageDisk import recupUsageDisk
from WindowsTools.windowsLogsCheck import list_evtx_files
from WindowsTools.windowsLogsCheck import show_list
from WindowsTools.windowsLogsCheck import check_all_evtx
from WindowsTools.windowsUpdate import checkUpdates

LOGS_PATH = r"C:\Windows\System32\winevt\Logs"


def main():
    print("Bienvenue")

    while True:
        print("---------Commandes-------------")
        print("Charge CPU : chargeCPU")
        print("Charge RAM: chargeRAM")
        print("Disk Usage : diskUsage")
        print("Check windows updates : checkWindowsUpdates")
        print("Windows Logs list : windowsLogs")
        print("Windows Logs integrity : windowsLogsCheck")
        print("Arret : 0")


        command = input("-------Entrez votre commande------\n>> ").strip()

        if command == "chargeCPU":
            charge(True)
        elif command == "chargeRAM":
            charge(False, True)
        elif command == "diskUsage":
            usage(True)
        elif command == "checkWindowsUpdates":
            windowsTools(False, False, True)
        elif command == "windowsLogs":
            windowsTools(False, True)
        elif command == "windowsLogsCheck":
            windowsTools(True)
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


def windowsTools(check=False, list=False, update=False):
    if check:
        try:
            logs_path_list = list_evtx_files(LOGS_PATH)
            check_all_evtx(logs_path_list)
        except Exception as e:
            print(f"Une erreur est survenue, veuillez essayer dans quelques instants. {e}")

    if list:
        try:
            logs_path_list = list_evtx_files(LOGS_PATH)
            show_list(logs_path_list)
        except Exception as e:
            print(f"Une erreur est survenue, veuillez essayer dans quelques instants. {e}")

    if update:
        try:
            checkUpdates()
        except Exception as e:
            print(f"Une erreur est survenue, veuillez essayer dans quelques instants. {e}")




if __name__ == '__main__':
    main()