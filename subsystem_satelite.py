'''
This file is created for AlbertaSat Ex-3 software team new member on board project.

Description: it simulates a TCP(Transmission Communication Protocol) between the ground
            station and satellite. The client/satellite will continuously send geo location
            and satellite status to the ground station along with receive current time from
            ground station
'''
import socket

from subsystem_command import Command
IP = socket.gethostname()
ADDRESS = 1025
satellite = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #  establish a TCP socket
satellite.connect((IP, ADDRESS)) #  connect the satellite to ground server

c = Command()


while True: #  the connection should always be established
    current_time = satellite.recv(40) # OBC receive 30 bytes information such that is current time
    print(current_time.decode("utf-8")) #  decode the time for testing purposes
    satellite.send(bytes(str(c.get_geo_location()), "utf-8")) #  send the satellite current geo location and state to the ground station
    satellite.send(bytes(str(c.get_satellite_state()), "utf-8"))
