# We have a loud talking parrot. 
# The "hour" parameter is the current hour time in the range 0..23. 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
# Return True if we are in trouble.

# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False
def parrot_trouble(str,hour):
    if str == True:
        if (hour < 7 or hour >20):
            return True
    
        else:
            return False 
 
        
    else:
        return False

print(parrot_trouble(True,6)) #True
print(parrot_trouble(True,6)) # True
print(parrot_trouble(True,7)) # False
print(parrot_trouble(False,6)) # False
print(parrot_trouble(True,21)) # True
print(parrot_trouble(False,21)) # False
print(parrot_trouble(True,20)) # False
print(parrot_trouble(True,23)) # True
print(parrot_trouble(True,0)) # True

# FEEDBACK: We went over this in 2/1/25 class
