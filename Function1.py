def convert_temperature(temperature, unit):
    if unit == "C":
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif unit == "F":
        celsius = (temperature - 32) * 5/9
        return celsius
    else:
        return "Invalid unit"
