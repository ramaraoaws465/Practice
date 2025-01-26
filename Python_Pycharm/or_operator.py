# logical operators or, and, not

# Or

print("Enter the Temperature value")
Temp = float(input("Temperature value : "))
is_raining = False

if Temp >= 35 or Temp < 0 or is_raining:
    print("the outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")