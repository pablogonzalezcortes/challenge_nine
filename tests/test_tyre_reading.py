from lib.tyre_reading import TyreReading


def test_initialization():
    tyre_reading = TyreReading()
    assert isinstance(tyre_reading, TyreReading)


def test_has_properties():
    tyre_reading = TyreReading()
    assert hasattr(tyre_reading, "_pressure")
    assert hasattr(tyre_reading, "_tread_depth")
    assert hasattr(tyre_reading, "_date")