import win32com.client

def get_cpu_model():
    try:
        # Connexion au service WMI
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")

        # Récupérer les informations sur le processeur
        cpu_info = service.ExecQuery("SELECT * FROM Win32_Processor")
        for cpu in cpu_info:
            print(f"CPU : {cpu.Name}")


    except Exception as e:
        print(f"Erreur lors de la récupération du processeur: {e}")

def get_disk_model():
    try:
        # Connexion au service WMI
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")

        # Récupérer les informations sur le disque
        disk_info = service.ExecQuery("SELECT * FROM Win32_DiskDrive")

        for disk in disk_info:
            print(f"HDD/SSD: {disk.Model}\n-------------")


    except Exception as e:
        print(f"Erreur lors de la récupération des informations disque: {e}")



def get_gpu_model():
    try:
        # Connexion au service WMI
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")

        # Récupérer les informations sur la carte graphique (Win32_VideoController)
        gpu_info = service.ExecQuery("SELECT * FROM Win32_VideoController")

        for gpu in gpu_info:
            print(f"GPU : {gpu.Name}")

    except Exception as e:
        print(f"Erreur lors de la récupération des informations sur la carte graphique: {e}")

def get_ram_model():
    try:
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")

        ram_info = service.ExecQuery("SELECT * FROM Win32_PhysicalMemory")

        for ram in ram_info:
            print(f"RAM : {ram.Model}")

    except Exception as e:
        print(f"Erreur lors de la récupération des informations sur la RAM: {e}")


def get_motherboard_model():
    try:
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")

        motherboard_info = service.ExecQuery("SELECT * FROM Win32_MotherboardDevice")

        for motherboard in motherboard_info:
            print(f"-------------\nMotherboard: {motherboard.Name}")

    except Exception as e:
        print(f"Erreur lors de la récupération des informations sur la MB: {e}")




