from lib.tyre_reading import TyreReading

class Tyre:
    def __init__(self, position):
        self.position = position 
        self.readings = []
        self.tyre_reading = TyreReading()

    def add_reading(self, pressure, tread_depth, reading_date):
        self.tyre_reading._pressure = pressure
        self.tyre_reading._tread_depth = tread_depth
        self.tyre_reading._date = reading_date
        self.readings.append({
            "reading_date": self.tyre_reading._date,
            "tyre_position": self.position,
            "tyre_pressure": self.tyre_reading._pressure,
            "tread_depth": self.tyre_reading._tread_depth
        })