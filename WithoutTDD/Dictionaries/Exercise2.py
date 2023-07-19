values={
    'centimeters': 100,
    'meters':1000,
    'kilometers':100000
}

value=float(input("Enter the value to convert: \n"))


value_in_c_to_m = value/values['centimeters']
print("Value in centimeters to value in meters:\n", value_in_c_to_m)

value_in_c_to_k = value/values['centimeters']/values['kilometers']
print("Value in centimeters to value in kilometers:\n", value_in_c_to_k)

value_in_m_to_c = value*values['meters']
print("Value in meters to value in centimeters:\n", value_in_m_to_c)

value_in_m_to_k = value/values['meters']
print("Value in meters to value in kilometers:\n", value_in_m_to_k)

value_in_k_to_c = value*values['kilometers']
print("Value in kilometers to value in centimeters:\n", value_in_k_to_c)

value_in_k_to_m = value*values['meters']/values['kilometers']
print("Value in kilometers to value in meters:\n", value_in_k_to_m)
