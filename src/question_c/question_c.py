#write functions here, don't add input('') statements here!
from main import get_bonus_pay
def test_configC():
    if get_bonus_pay(-1)=="Invalid Arguments":
        if get_bonus_pay(200)==10:
            if get_bonus_pay(600)==36:
                if get_bonus_pay(1000)==70:
                    if get_bonus_pay(1500)==120:
                        if get_bonus_pay(2000)=="Invalid Arguments":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False