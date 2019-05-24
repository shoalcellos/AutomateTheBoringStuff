# Strong Password Detection
# https://automatetheboringstuff.com/chapter7/

import re
def isStrongPass(password):
    if len(password) > 8:
        if re.match(r".*[A-Z]+.*", password) != None:
            if re.match(r".*[a-z]+.*", password) != None:
                if re.match(r".*\d+.*", password) != None:
                    return True 
    return False

assert isStrongPass("phdagsfdvfenK12") == True