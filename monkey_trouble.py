# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling.
#  Return True if we are in trouble.


# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

# Function to determine if we are in trouble based on the monkeys' smiles
def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile:
        return True

    if not a_smile and not b_smile:
        return True

    else:
        return False

if __name__ == '__main__':
    print("Are the two monkeys staring at us?")

    print(monkey_trouble(False,False))

# FEEDBACK
# Overall looks good 
# One suggestion is to combine the two if statements into one if statement:
# if (a_smile and b_smile) or (not a_smile and not b_smile):
#     return True
# else:
#     return False
