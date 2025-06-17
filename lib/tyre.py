from lib.tyre_reading import TyreReading

class Tyre:
    def __init__(self, position):
        self.position = position 
        self.readings = []
        self.tyre_reading = TyreReading()