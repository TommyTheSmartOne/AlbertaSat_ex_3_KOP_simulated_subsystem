'''
This file is created for AlbertaSat Ex-3 software team new member on board project.

Description: This file contains all the function that will be needed based on the KOP
            description, that is:
            1. A command to get stored UTC time and send it to the OBC
            2. Be able to send latitude and longitude data
            3. Return state (on/off)
            4. Send an ACK when pinged
            Since it is for simulation/test purpose, the geo graphic information and satellite
            state will be random(I choose decimal format coordinate of North pole)

Author: MingLiang Wang
Date: 10/6/2024
'''
from datetime import datetime
import keyboard


class Command:
    '''
    This class contains all the commands needed for the simulation
    '''
    def __init__(self):
        self.latitude = 0
        self.longitude = 0
        self.satellite_state = "off"

    def startDrone(self):
        self.set_satellite_state()


    def get_time(self):
        '''
        This function returns current UTC time
        '''
        return datetime.now()

    def get_satellite_state(self):
        '''
        This function returns the satellite current state
        The satellite can have 2 state:
            on
            off
        '''
        return self.satellite_state

    def get_geo_location(self):
        '''
        This function gets the geo location() date from satellite
        The geo location consists 2 float:
            Latitude: -1.2832533
            Longitude: 36.8172449
        There are library that supports to find real time
        location, but based on the KOP description the ex-3
        will have a GPS system, thus the data we are using
        is random
        '''
        return self.latitude, self.longitude

    def set_geo_location(self, latitude, longitude):
        '''
        This function sets the satellites geo location
        The geo location consists 2 float:
            Latitude: -1.2832533
            Longitude: 36.8172449
        '''
        self.latitude = latitude
        self.longitude = longitude

    def set_satellite_state(self):
        '''
        This function sets satellite current state
         The satellite can have 2 state:
            on
            off
        '''
        if self.satellite_state == "off": #  since the satellite only have 2 states, this function acts like
            # a switch each time we call this function we will change the state of the satellite
            self.satellite_state = "on"
        else:
            self.satellite_state = "off"

    def sendDirectionCommand(self):
        if keyboard.is_pressed('w'):
            return "Foward"
        elif keyboard.is_pressed('a'):
            return "Left"
        elif keyboard.is_pressed('d'):
            return "Right"
        elif keyboard.is_pressed('s'):
            return "Backward"
        elif keyboard.is_pressed('u'):
            return "Up"
        elif keyboard.is_pressed('j'):
            return "down"

        return "on hold"
    # def send_ACK():
