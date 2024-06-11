'''
This file is created for AlbertaSat Ex-3 software team new member on board project.

Description: it simulates a TCP(Transmission Communication Protocol) between the ground
            station and satellite. The client/satellite will continuously send geo location
            and satellite status to the ground station along with receive current time from
            ground station

Author: MingLiang Wang
Date: 10/6/2024
'''
import socket
from time import sleep
from subsystem_command import Command

IP = socket.gethostname()
ADDRESS = 1026
c = Command()

satellite = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # establish a TCP socket
satellite.connect((IP, ADDRESS))  # connect the satellite to ground server

last_time = c.get_time()  # initial time when the connection is established
while True:  # the connection should always be established
    satellite.send(bytes(str(c.get_geo_location()), "utf-8"))  # send the satellite current geo location and state to
    # the ground station
    satellite.send(bytes(str(c.get_satellite_state()), "utf-8"))
    sleep(0.1)
    # I added this sleep is because even though it is a while true loop the iteration seems to stuck
    # at some point, I suspect it is due to the sending and recv data is done too fast and when recv 2 consecutive
    # data and the constrain for recv data is set to equal or higher than the bytes sum of two data, the code will
    # store both data in geo_location, thus nothing will goes to satellite_state and yet the server is still awaiting
    # thus it seems like the while loop is "stuck"
    current_time = satellite.recv(40)  # OBC receive 30 bytes information such that is current time: #  update
    # last_time and print out current time iff the time we received differs from previous time
    print(current_time.decode("utf-8"))  # decode the time for testing purposes
