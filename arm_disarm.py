from dronekit import connect, VehicleMode
import time
from status import uav

"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
connection_string=s.getsockname()[0] + ":14550"
#connection_string="127.0.0.1:14550"
uav=connect(connection_string,wait_ready=True,timeout=100)
"""

def arm_disarm():
    print("ARM DISARM")

    while uav.is_armable==False:
        print("Cannot Armable")
        time.sleep(1)
    print("UAV can Arm")

    uav.mode=VehicleMode("GUIDED")
    while uav.mode!="GUIDED":
        print('Changing Mode to GUIDED')
        time.sleep(1.5)
    print("Mode Changed to GUIDED")

    uav.armed=True
    while uav.armed is False:
        print("Waiting for Arm")
        time.sleep(1)
    print("UAV Armed !")

    time.sleep(5)

    uav.armed=False
    while uav.armed is True:
        print("Waiting for Disarm")
        time.sleep(1)
    print("UAV Disarmed !")

    uav.mode=VehicleMode("STABILIZE")
    while uav.mode!="STABILIZE":
        print('Changing Mode to STABILIZE')
        time.sleep(1.5)
    print("Mode Changed to STABILIZE")

    print("Exiting ...")



#arm_disarm()