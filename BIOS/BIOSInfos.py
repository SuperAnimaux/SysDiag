import win32com.client

def get_BIOS_infos():
    try:
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")

        BIOS_infos = service.ExecQuery("SELECT * FROM Win32_BIOS")

        for BIOS in BIOS_infos:
            print(f"-------------\nBIOS name: {BIOS.Name}\nBIOS version : {BIOS.BIOSVersion}\nManufacturer : {BIOS.Manufacturer}\nSerial number : {BIOS.SerialNumber}\nStatus : {BIOS.Status}")

    except Exception as e:
        print(e)

