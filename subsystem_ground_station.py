'''
This file is created for AlbertaSat Ex-3 software team new member on board project.

Description: it simulates a TCP(Transmission Communication Protocol) between the ground
            station and satellite. The server will continuously send Mountain - AB; BC (E);
            NT (E); SK (W) time information to the satellite as well as receive the geo
            location and satellite status from satellite
'''
import socket
from subsystem_command import Command

IP = socket.gethostname()
ADDRESS = 1025
ground_station = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ground_station.bind((IP, ADDRESS))
ground_station.listen(10)

satellite, address = ground_station.accept() #  establish a connection between server and satellite
print("Connection established")

c = Command()
while True:
    TIME = str(c.get_time())
    satellite.send(bytes(TIME, "utf-8")) #  send current time to the satellite
    geo_location = satellite.recv(40).decode("utf-8")
    print(geo_location)
    satellite_state = satellite.recv(40).decode("utf-8")
    print(satellite_state)
