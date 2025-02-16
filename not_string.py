# Given a string, return a new string where "not " has been added to the front.
#  However, if the string already begins with "not", return the string unchanged.


# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):

    if len(str) >= 1:
        if str[:3] == "not":
            return str
        
        else:
            return "not " + str
    else:
        pass

print(not_string("Candy"))

print(not_string("x"))

print(not_string('not bad'))    