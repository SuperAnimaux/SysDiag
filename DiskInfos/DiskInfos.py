import win32com.client

def get_disk_infos():

    wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    service = wmi.ConnectServer(".", "root\\cimv2")

    disk_infos = service.ExecQuery("SELECT * FROM Win32_DiskDrive")

    for disk in disk_infos:
        print(f"-----------\nDisk Model : {disk.Model}\nDisk manufacturer : {disk.Manufacturer}\nSerial number : {disk.SerialNumber}\nDisk Name : {disk.Name}\nDisk Size : {int(disk.Size) / (1024 ** 3)} GB\nDisk status : {disk.Status} \nAvailability : Code {disk.Availability} (Read disk.md)")


