from dronekit import connect, VehicleMode
from status import uav
from pymavlink import mavutil
import time

"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
connection_string=s.getsockname()[0] + ":14550"
#connection_string="127.0.0.1:14550"
uav=connect(connection_string,wait_ready=True,timeout=100)
"""

def land():
	print("LAND")

	uav.mode=VehicleMode("LAND")
	while uav.mode != "LAND":
		print("Changing Mode to LAND")
		time.sleep(1.5)
	print("Mode Changed to LAND")

	while uav.location.global_relative_frame.alt >= 0.1:
		print("Landing, Altitude : {}".format(uav.location.global_relative_frame.alt))
		time.sleep(1.5)
	print("Landed")

	uav.armed=False
	while uav.armed is True:
		print("Waiting for Disarm")
		time.sleep(1)
	print("UAV Disarmed !")

	uav.mode=VehicleMode("STABILIZE")
	while uav.mode != "STABILIZE":
		print("Changing Mode to STABILIZE")
		time.sleep(1.5)
	print("Mode Changed to STABILIZE")
	print("Exiting ...")



#land()