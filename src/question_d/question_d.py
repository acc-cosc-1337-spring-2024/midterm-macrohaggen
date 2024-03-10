#write functions here, don't add input('') statements here!
from main import get_assessment_value
from main import get_tax_assessed
def test_configD():
    if get_assessment_value(10000)==6000:
        if get_assessment_value(20000)==12000:
            if get_tax_assessed(6000)==43.2:
                if get_tax_assessed(10000)==72:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False