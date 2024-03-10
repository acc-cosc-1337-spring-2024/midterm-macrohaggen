#write functions here, don't add input('') statements here!
from main import get_miles_per_hour
def test_configB():
    if get_miles_per_hour(32, 60)==19.883872:
        return True
    else:
        return False