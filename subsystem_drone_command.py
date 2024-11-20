

class Command:
    def __init__(self):
        self.x = 0.0000
        self.y = 0.0000
        self.z = 0.0000
        self.satellite_state = 0

    def startDrone(self):
        self.set_satellite_state()

    def set_satellite_state(self, state):
        '''
        This function sets satellite current state
         The satellite can have 2 state:
            on
            off
        '''
        self.satellite_state = state

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
        return self.x, self.y, self.z

    def get_satellite_state(self):
        '''
        This function returns the satellite current state
        The satellite can have 2 state:
            on
            off
        '''
        return self.satellite_state

