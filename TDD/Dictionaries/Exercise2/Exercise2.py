def centimeters_to_meters(value):
    return value / 100

def centimeters_to_kilometers(value):
    return value / 100000

def meters_to_centimeters(value):
    return value * 100

def meters_to_kilometers(value):
    return value / 1000

def kilometers_to_centimeters(value):
    return value * 100000

def kilometers_to_meters(value):
    return value * 1000

if __name__ == "__main__":
    values = {
        'centimeters': 100,
        'meters': 1000,
        'kilometers': 100000
    }

    value = float(input("Enter the value to convert: \n"))

    value_in_c_to_m = centimeters_to_meters(value)
    print("Value in centimeters to value in meters:\n", value_in_c_to_m)

    value_in_c_to_k = centimeters_to_kilometers(value)
    print("Value in centimeters to value in kilometers:\n", value_in_c_to_k)

    value_in_m_to_c = meters_to_centimeters(value)
    print("Value in meters to value in centimeters:\n", value_in_m_to_c)

    value_in_m_to_k = meters_to_kilometers(value)
    print("Value in meters to value in kilometers:\n", value_in_m_to_k)

    value_in_k_to_c = kilometers_to_centimeters(value)
    print("Value in kilometers to value in centimeters:\n", value_in_k_to_c)

    value_in_k_to_m = kilometers_to_meters(value)
    print("Value in kilometers to value in meters:\n", value_in_k_to_m)
