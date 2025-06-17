from lib.tyre import Tyre
from lib.tyre_reading import TyreReading

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
    tyre.add_reading("2.3 bar", "2 mm", [DATE?])