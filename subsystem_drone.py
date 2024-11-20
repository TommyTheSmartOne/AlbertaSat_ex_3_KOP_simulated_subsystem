'''
This file is created for AlbertaSat Ex-3 software team new member on board project.

Description: it simulates a TCP(Transmission Communication Protocol) between the ground
            station and drone. The client/drone will continuously send geo location
            and drone status to the ground station along with receive current time from
            ground station

Author: MingLiang Wang
Date: 10/6/2024
'''
import socket
from time import sleep
from subsystem_drone_command import Command

IP = "192.168.137.1"
print(IP)
ADDRESS = 5005
c = Command()

drone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # establish a TCP socket
drone.connect((IP, ADDRESS))  # connect the drone to ground server


def startDrone():
    while 1:
        state = drone.recv(40)
        if state:
            c.set_satellite_state(1)
            return


startDrone()

while 1:  # the connection should always be established
    drone.send(bytes(str(c.get_geo_location()), "utf-8"))  # send the drone current geo location and state to
    # the ground station
    drone.send(bytes(str(c.get_satellite_state()), "utf-8"))
    sleep(0.1)
    # I added this sleep is because even though it is a while true loop the iteration seems to stuck
    # at some point, I suspect it is due to the sending and recv data is done too fast and when recv 2 consecutive
    # data and the constrain for recv data is set to equal or higher than the bytes sum of two data, the code will
    # store both data in geo_location, thus nothing will goes to satellite_state and yet the server is still awaiting
    # thus it seems like the while loop is "stuck"
    direction_command = drone.recv(40)
    print(direction_command.decode("utf-8"))  # decode the time for testing purposes
