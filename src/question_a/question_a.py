#write functions here, don't add input('') statements here!
from main import is_prime
def test_config():
    if is_prime(4)==False:
        if is_prime(5)==True:
            if is_prime(11)==True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False