
# write a program to find the wind chill
def windchill(v,t):
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16
    return w

v = int(input("Enter wind spedd v: "))
t= int(input("Enter temperature t: "))

if v > 120 or v<3 or t>50:
    print("Enter valid wind speed")
else:
    print("windd chill is", windchill(v,t))