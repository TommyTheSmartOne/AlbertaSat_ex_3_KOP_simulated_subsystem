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
import keyboard


class Command:
    '''
    This class contains all the commands needed for the simulation
    '''

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
