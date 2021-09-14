from dronekit import connect
uav = None

def getUAV():
    global uav
    return uav

def setUAV(drone):
    global uav
    uav.close()
    uav = drone

def connection(connection_string):
    global uav
    if connection_string != None:
        uav=connect(connection_string, wait_ready=True, timeout=100)
        
