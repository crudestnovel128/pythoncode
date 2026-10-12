# TEMPERATURE CONVERTER
temperature = float(input("Enter temperture (Celsius or Fahrenheit): "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")
if unit == "C" or unit == "c":
    temperature_in_fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature} Celcius is equal to {round(temperature_in_fahrenheit, 2)}")
elif unit == "F" or unit == "f":
    temperature_in_celsius = (temperature - 32) * 5/9
    print(f"{temperature} Fahrenheit is equal to {round(temperature_in_celsius, 2)}")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")    