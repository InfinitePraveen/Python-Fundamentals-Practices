# Convert Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32
#
# 1. Store 25°C in a variable
# 2. Calculate Fahrenheit
# 3. Print: "25°C is 77.0°F"

c = input("Enter the value of Celcius\n(Which you want to convert in Farhenhier):")
c = float(c)
F = (c * 9/5) + 32
print(f"The Farhenheit of {c}° Celcius is {F}° Farenheit.")