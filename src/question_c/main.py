#add import
def get_bonus_pay(sales):
    str = "Invalid Arguments"
    sperc = 0
    if sales>0:
        if sales>=500:
            if sales>=1000:
                if sales>=1500:
                    if sales>=2000:
                        return str
                    else:
                        sperc = sales*0.08
                        return int(sperc)
                else:
                        sperc = sales*0.07
                        return int(sperc)
            else:
                        sperc = sales*0.06
                        return int(sperc)
        else:
                        sperc = sales*0.05
                        return int(sperc)
    else:
          return str
sqc = int(input("Enter Sales Quanta:\n"))
print(get_bonus_pay(sqc))