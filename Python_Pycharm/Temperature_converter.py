from math import degrees

unit = input("Is this temeprature is celisus or Faranheit(C/F): ")
temp = float(input("Enter the temperature: "))
degrees_symbol = "\u00b0"

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Farenheit is : {temp} {degrees_symbol}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The Temperature in Celsius is: {temp} {degrees_symbol}C")

else:
    print(f"{unit} is an invalid unit of measurement")
