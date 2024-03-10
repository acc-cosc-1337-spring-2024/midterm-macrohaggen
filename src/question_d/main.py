#add import
def get_assessment_value(price):
    apr = 0
    apr = price*0.6
    return int(apr)
def get_tax_assessed(Aprice):
    Tprice = 0
    Tprice = Aprice//100
    Tprice *= 0.72
    return round(Tprice, 2)
none = 1
while none == 1:
    value = int(input("Enter Property Value:\n"))
    print("Assessed Value:", get_assessment_value(value))
    print("Assessed Taxation:", get_tax_assessed(get_assessment_value(value)))
    if str(input("End? (y/n)\n"))=="y":
        none == 0
    else:
        continue