def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
    #  F = (°C × 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
    # C = (°F - 32) × 5/9

def convert_temperature():

    tem_val = float(input("Enter the Tempareture Value : "))
    unit = input("Enter ( C for Celsius and F for faharenheit) : ").upper

    if unit = "C":
convert_temp = fahrenheit_to_celsius(tem_val) 