#add import
def get_miles_per_hour(km, min):
    str == 'Invalid Arguments'
    if km<0 or min<0:
        return str
    else:
        miles = km*0.621371
        hours = min/60
        return miles/hours
none = 1
while none == 1:
    kilo = int(input("Enter Kilometers:\n"))
    minos = int(input("Enter Minutes:\n"))
    print("Miles per hour:", get_miles_per_hour(kilo, minos))
    if str(input("End? (y/n)\n"))=="y":
        none = 0
    else:
        continue