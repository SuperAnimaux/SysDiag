import win32com.client
from datetime import datetime

def get_gpu_infos():
    wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    service = wmi.ConnectServer(".", "root\\cimv2")

    gpu_infos = service.ExecQuery("Select * From Win32_VideoController")

    for gpu in gpu_infos:
        print(f"----------\nGPU Model : {gpu.Name}\n---------GPU Architecture---------\nGPU architecture : Code {gpu.VideoArchitecture} (Read gpu.md)\nGPU processor : {gpu.VideoProcessor}\nMin refresh rate : {gpu.MinRefreshRate} Hz\nMax refresh rate : {gpu.MaxRefreshRate} Hz\n---------GPU Memory---------\nGPU memory type : Code {gpu.VideoMemoryType} (Read gpu.md)\nGPU memory size : {int(gpu.AdapterRAM) / (1024 ** 3)} GB\nMax supported memory: {gpu.MaxMemorySupported} bytes\n---------GPU Driver---------\nGPU Driver path : {gpu.InstalledDisplayDrivers}\nDriver version : {gpu.DriverVersion}\nLast update at : {datetime.strptime(gpu.DriverDate.split('-')[0], '%Y%m%d%H%M%S.%f')}\n---------GPU Availability---------\nGPU Status : {gpu.Status}\nGPU availability : code {gpu.Availability} (Read gpu.md")



