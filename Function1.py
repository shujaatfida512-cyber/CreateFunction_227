def convert_temperature(temperature, unit):
    if unit == "C":
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif unit == "F":
        celsius = (temperature - 32) * 5/9
        return celsius
    else:
        return "Invalid unit"

temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

result = convert_temperature(temperature, unit)

if unit == "C":
    print("Temperature in Fahrenheit:", result)
elif unit == "F":
    print("Temperature in Celsius:", result)
else:
    print(result)