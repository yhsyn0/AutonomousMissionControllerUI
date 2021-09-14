from dronekit import connect, VehicleMode
from status import uav
from pymavlink import mavutil
import time
import math

"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
connection_string=s.getsockname()[0] + ":14550"
#connection_string="127.0.0.1:14550"
uav=connect(connection_string,wait_ready=True,timeout=100)
"""

altitude = 5

def arm_takeoff(altitude):
	print("FLY AROUND SQUARE")

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
	
	uav.simple_takeoff(altitude)
	while uav.location.global_relative_frame.alt<=altitude*0.94:
		print("Current Altitude : {}".format(uav.location.global_relative_frame.alt))
		time.sleep(0.5)
	print("Takeoff Initialized")



def targetPos(pos_x, pos_y, pos_z, yaw_rate):
	msg = uav.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
          0b0000011111111000,
          pos_x, pos_y, pos_z, #pozisyonlar(metre)
          0, 0, 0,
          0, 0, 0,
          0, math.radians(yaw_rate))

	uav.send_mavlink(msg)
	

def movePoints():
	targetPos(5,0,-altitude,0)
	while uav.location.local_frame.north<=4.9:
		print("Not in the North Position")
		targetPos(5,0,-altitude,0)
		time.sleep(2)

	targetPos(5,5,-altitude,0)
	while uav.location.local_frame.east<=4.9:
		print("Not in the East Position")
		targetPos(5,5,-altitude,0)
		time.sleep(2)

	targetPos(0,5,-altitude,0)
	while uav.location.local_frame.north>=0.1:
		print("Not in the South Position")
		targetPos(0,5,-altitude,0)
		time.sleep(2)
	
	targetPos(0,0,-altitude,0)
	while uav.location.local_frame.east>=0.1:
		print("Not in the West Position")
		targetPos(0,0,-altitude,0)
		time.sleep(2)



def land():
	time.sleep(10)

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

	

#arm_takeoff(altitude)
#time.sleep(5)
#movePoints()
#land()