'''
This file is created for AlbertaSat Ex-3 software team new member on board project.

Description: it simulates a TCP(Transmission Communication Protocol) between the ground
            station and drone. The server will continuously send Mountain - AB; BC (E);
            NT (E); SK (W) sudotime information to the drone as well as receive the geo
            location and drone status from drone

Author: MingLiang Wang
Date: 10/6/2024
'''
import socket
from subsystem_command import Command

IP = "172.28.172.229"
ADDRESS = 5005
ground_station = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ground_station.bind((IP, ADDRESS))
ground_station.listen(10)

print(f"Server running at {IP}:{ADDRESS}")
drone, address = ground_station.accept() #  establish a connection between server and drone
print("Connection established")

c = Command()


while True:
    #drone.send(bytes(TIME, "utf-8")) #  send current time to the drone
    drone.send(bytes(c.sendDirectionCommand(), "utf-8"))
    geo_location = drone.recv(40).decode("utf-8")
    if ground_station:
        print(geo_location)
    satellite_state = drone.recv(40).decode("utf-8")
    if satellite_state:
        print(satellite_state)

