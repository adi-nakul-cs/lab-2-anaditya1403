# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]

if __name__ == "__main__":
    print(front_back("Adity"))

    print(front_back("Zebra"))

    print(front_back("Xenon"))

    print(front_back("A"))

    print(front_back("ab"))
#All test cases are running as expected