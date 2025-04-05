
import ctypes
from DiskInfos.diskUsage import recupUsageDisk
from DiskInfos.DiskInfos import get_disk_infos
from CPUInfos.CPUInfos import get_CPU_infos
from GPUInfos.GPUInfos import get_gpu_infos
from RAMInfos.RAMInfos import get_RAM_infos
from WindowsTools.windowsLogsCheck import list_evtx_files
from WindowsTools.windowsLogsCheck import show_list
from WindowsTools.windowsLogsCheck import check_all_evtx
from WindowsTools.windowsUpdate import checkUpdates
from hardwareInfos.modelInfos import get_all_models
from BIOS.BIOSInfos import get_BIOS_infos


LOGS_PATH = r"C:\Windows\System32\winevt\Logs"


def main():
    print("Bienvenue")

    while True:
        print("---------Command-------------\nHardware information : hardwareInfos\nBios information : biosInfos\nCPU information : cpuInfos\nGPU information : gpuInfos\nRAM information : ramInfos\nDisk information : diskInfos\nDisk Usage : diskUsage\nCheck windows updates : checkWindowsUpdates\nWindows Logs list : windowsLogs\nWindows Logs integrity : windowsLogsCheck\nExit : 0")


        command = input("-------Enter instruction------\n>> ").strip()

        if command == "hardwareInfos":
            hardwareInfos(True)
        elif command == "biosInfos":
            hardwareInfos(False, True)
        elif command == "cpuInfos":
            CPU_infos()
        elif command == "gpuInfos":
            gpu_infos()
        elif command == "ramInfos":
            ram_infos()
        elif command == "diskInfos":
            diskTools(False, True)
        elif command == "diskUsage":
            diskTools(True)
        elif command == "checkWindowsUpdates":
            windowsTools(False, False, True)
        elif command == "windowsLogs":
            windowsTools(False, True)
        elif command == "windowsLogsCheck":
            windowsTools(True)
        elif command == "0":
            break



def ram_infos():
    try:
        get_RAM_infos()
    except Exception as e:
        print(f"An error has occurred : {e}")


def gpu_infos():
    try:
        get_gpu_infos()
    except Exception as e:
        print(f"An error has occurred : {e}")


def CPU_infos():
    try:
        get_CPU_infos()
    except Exception as e:
        print(f"An error has occurred : {e}")


def diskTools(usage=False, infos=False):
    if usage:
        try:
            usageDisk = recupUsageDisk()
            print(f"disk usage : {usageDisk}%")
        except Exception as e:
            print(f"An error has occurred : {e}")

    if infos:
        try:
            get_disk_infos()
        except Exception as e:
            print(f"An error has occurred : {e}")


def windowsTools(check=False, list=False, update=False):

    if check:
        if is_program_admin():
            try:
                logs_path_list = list_evtx_files(LOGS_PATH)
                check_all_evtx(logs_path_list)
            except Exception as e:
                print(f"An error has occurred : {e}")
        else:
            print("administrator permission required")

    if list:
        try:
            logs_path_list = list_evtx_files(LOGS_PATH)
            show_list(logs_path_list)
        except Exception as e:
            print(f"An error has occurred : {e}")

    if update:
        try:
            print("Please wait...")
            checkUpdates()
        except Exception as e:
            print(f"An error has occurred : {e}")

def hardwareInfos(hardware=False, bios=False):
    if hardware:
        try:
            get_all_models()

        except Exception as e:
            print(f"An error has occurred : {e}")

    if bios:
        try:
            get_BIOS_infos()
        except Exception as e:
            print(f"An error has occurred : {e}")

def is_program_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"An error has occurred : {e}")
        return False


if __name__ == '__main__':
    main()