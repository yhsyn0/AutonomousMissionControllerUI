from connect import uav
import socket
from dronekit import connect
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(('8.8.8.8', 1))
#connection_string=s.getsockname()[0] + ":14550"
connection_string="192.168.4.2:14550"
uav=connect(connection_string,wait_ready=True,timeout=100)


def battery_stats():
    if uav != None:
        return uav.battery

def mode_name():
    if uav != None:
        return uav.mode.name

def loc_local():
    if uav != None:
        return uav.location.local_frame


def loc_global():
    if uav != None:
        return uav.location.global_frame

def arm_status():
    if uav != None:
        if uav.armed == True:
            return "Armed"
        elif uav.armed == False:
            return "Disarmed"
