import time
import socket
import math

#####################PARTS OF THE DRONE TO BE CONNECTED TO THE CONTROL SOFTWARE####################

class PARTS:

    PART_1: str = 'ELECTRONIC SPEED CONTRLLER'
    PART_2: str = 'AURDUINO UNO'
    PART_3: str = 'RADIO TRANSMITTER'
    PART_4: str = 'SENSORS'
    PART_5: str = 'CAMERA'
    PART_6: str = 'FLIGHT DATA'
    PART_7: str = 'SERVO MOTOR'
    PART_8: str = ''



####################BUILDING OF DRONE FUNCTIONS######################

def connect(ip_address: str, commands: str):
    # THE CONNECT FUNCTION TAKES IN THE IP ADDRESS OF A SENSOR OR DEVICE ON THE DESTAR DRONE, CONECTS WITH IT USING THE SOCKET MODULE AND ENABLE THE CONTROL SOFTWARE/PILOT TO SEND COMMANDS
    pass

open('C:\DESTAR_STATION\DESTAR_DRONE\Control_Software\DESTAR_DroneKit\Kit\servo.ino')