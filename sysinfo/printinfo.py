#!/usr/bin/python
import psutil
import json

class SysInfo:
    'Common base class for all SysInfos'
    empCount = 0
    os = __import__('os')
    psutil = __import__('psutil')
    # showitems: cpu, disk, memory, all; showoptions: b, kb, mb, gb
    def __init__(self, showoption):
        assert type(showoption) == str, "Error! Second value should be string."
        if showoption == 'kb':
            self.showoption = 2**10
        if showoption == 'mb':
            self.showoption = 2**20
        if showoption == 'gb':
            self.showoption = 2**30
        else:
            self.showoption = 1
        SysInfo.empCount += 1
        self.__data = {'Status': None,
                       'Content-Type': 'application/json',
                       'ShowOption': showoption,
                       'payload': {
                           'CpuUsage': None,
                           'TotalMemory': None,
                           'FreeMemory': None,
                           'UsedMemory': None,
                           'DiskSize': None,
                           'FreeSpace': None,
                           'UsedDisk': None
                       }}

    def __displayCpuInfo(self):
        try:
            self.__data['payload']['CpuUsage'] = round(psutil.cpu_percent(),2)
        except:
            self.__data['payload']['CpuUsage'] = "Failed"
        #        finally:
#            return
#        return self.__data

    def __displayMemInfo(self):
        try:
            self.__data['payload']['TotalMemory'] = round(psutil.virtual_memory().total / self.showoption, 2)
            self.__data['payload']['FreeMemory'] = round(psutil.virtual_memory().available / self.showoption, 2)
            self.__data['payload']['UsedMemory'] = round(psutil.virtual_memory().percent, 2)
        except:
            self.__data['payload']['TotalMemory'] = "Failed"
            self.__data['payload']['FreeMemory'] = "Failed"
            self.__data['payload']['UsedMemory'] = "Failed"
#        return self.__data

    def __displayDiskInfo(self):
        # [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')]
        # sdiskusage(total=255820034048, used=48093286400, free=207726747648, percent=18.8)
        try:
            for pts in psutil.disk_partitions():
                self.__data['payload']['DiskSize'] = round(psutil.disk_usage(pts.mountpoint).total / self.showoption, 2)
                self.__data['payload']['FreeSpace'] = round(psutil.disk_usage(pts.mountpoint).free / self.showoption, 2)
                self.__data['payload']['UsedDisk'] = round(psutil.disk_usage(pts.mountpoint).percent, 2)
        except:
            self.__data['payload']['DiskSize'] = "Failed"
            self.__data['payload']['FreeSpace'] = "Failed"
            self.__data['payload']['UsedDisk'] = "Failed"
#        return self.__data

    def displayInfo(self):
        try:
            self.__displayCpuInfo()
            self.__displayMemInfo()
            self.__displayDiskInfo()
            self.__data['Status'] = "SUCCESS"
        except Exception as e:
            self.__data['Status'] = getattr(e, 'message', repr(e))
        return json.dumps(self.__data)

