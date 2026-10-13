import numpy as np

#Triangular membership function
def triangular (x, a, b, c):
    if x<=a or x>=c:
        return 0
    elif x==b:
        return 1
    elif x<b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

#Take temperture from user
temperature_input = int(input("Enter temperature (c):"))

#Fan off condition
if temperature_input < 1:
    speed = 0
    print("\nFuzzy Control output")
    print("Temperature :", temperature_input, "c")
    print("Fan speed   : 0%")
    print("Fan status   : OFF")

#FUZZY CONTROL
else:
    #Membership values
    low = triangular(temperature_input, 1, 20, 40)
    medium = triangular(temperature_input, 20, 40, 60)
    high = triangular(temperature_input, 60, 80, 100)

    #Display membership values
    print("\nTemperature Membership values:")
    print("Low    :", round(low, 2))
    print("Medium :", round(medium, 2))
    print("High   :", round(high, 2))

# defuzzificatiin using weighted avrage
    total = low + medium + high
    if total != 0:
        speed = (low*25+medium*50+high*100)/total
    else:
         speed = 0

    #Display Fuzzy control output
    print("\nFuzzy Control output")
    print("Temperature  :", temperature_input, "c")
    print("Fan Speed    :", round(speed, 2), "%")

    #Detarmine fan status
    if speed <= 35:
        print("Fan status  : Slow")
    elif speed <= 70:
        print("Fan Status  : Medium")
    else:
        print("Fan Status  : Fast")
