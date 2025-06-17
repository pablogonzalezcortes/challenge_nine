from lib.tyre import Tyre
from lib.tyre_reading import TyreReading
from datetime import datetime

def test_initilization():
    tyre = Tyre("Front Left")
    assert isinstance(tyre, Tyre)


def test_tyre_class_has_instance_of_tyrereading():
    tyre = Tyre("Front Left")
    tyre_reading = tyre.tyre_reading
    assert isinstance(tyre_reading, TyreReading)


# TODO: decide whether #add_reading needs to have date as an arguement
def test_add_reading_adds_a_reading_to_tyrereading():
    tyre = Tyre("Front Left")
    reading_date_as_datetime_obj = datetime.strptime('2025-05-24', "%Y-%m-%d")
    tyre.add_reading("2.3 bar", "2 mm", reading_date_as_datetime_obj)
    assert tyre.readings[0] == {"reading_date": reading_date_as_datetime_obj, "tyre_position": "Front Left", "tyre_pressure": "2.3 bar", "tread_depth": "2 mm"}
