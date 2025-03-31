import win32com.client

def get_CPU_infos():
    try:
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")

        cpu_infos = service.ExecQuery("SELECT * FROM Win32_Processor")

        for cpu in cpu_infos:
            print(f"---------\nCPU name : {cpu.Name}\nArchitecture : Code {cpu.Architecture} (Read Processor.md)\nMax clock speed: {cpu.MaxClockSpeed} MHz\nManufacturer : {cpu.Manufacturer}\nCores : {cpu.NumberOfCores}\nStatus : {cpu.Status}\nAvailability : Code {cpu.Availability} (Read processor.md)")

    except Exception as e:
        print(f"An error has occurred : {e}")


