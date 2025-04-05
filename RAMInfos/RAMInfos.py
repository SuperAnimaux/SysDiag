import win32com.client

def get_RAM_infos():

    try:
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")

        ram_infos = service.ExecQuery("SELECT * FROM Win32_PhysicalMemory")

        for ram in ram_infos:
            print(f"------------\nRAM Model : {ram.Model}\nRAM Name : {ram.Name}\nRAM manufacturer : {ram.Manufacturer}\nSerial Number : {ram.SerialNumber}\nRAM type : Code {ram.MemoryType} (Read ram.md)\nRAM Size : {int(ram.Capacity) / (1024 ** 3)} GB\nRAM speed : {ram.Speed} MHz\nRAM status : {ram.Status}")
    except Exception as e:
        print(f"An error has occurred : {e}")

