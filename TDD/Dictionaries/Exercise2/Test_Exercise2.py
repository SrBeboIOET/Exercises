from Exercise2 import centimeters_to_meters, centimeters_to_kilometers, meters_to_centimeters, meters_to_kilometers, kilometers_to_centimeters, kilometers_to_meters

def test_centimeters_to_meters():
    value_in_cm = 100 #arrange

    result = centimeters_to_meters(value_in_cm) #act

    assert result == 1 #assert

def test_centimeters_to_kilometers():
    value_in_cm = 100000 #arrange

    result = centimeters_to_kilometers(value_in_cm) #act

    assert result == 1 #assert

def test_meters_to_centimeters():
    value_in_m = 1

    result = meters_to_centimeters(value_in_m)

    assert result == 100

def test_meters_to_kilometers():
    value_in_m = 1000

    result = meters_to_kilometers(value_in_m)

    assert result == 1

def test_kilometers_to_centimeters():
    value_in_km = 1

    result = kilometers_to_centimeters(value_in_km)

    assert result == 100000

def test_kilometers_to_meters():
    value_in_km = 1

    result = kilometers_to_meters(value_in_km)

    assert result == 1000
