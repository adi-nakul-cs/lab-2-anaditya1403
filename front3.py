# Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. 
# Return a new string which is 3 copies of the front.


# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'

def front(str):
    front = str[:3]
    if len(front) > 2:
        return front * 3 
    else:
        return str
    
if __name__ == "__main__":
    print(front("Chocolate"))

    print(front("Java"))

    print(front("Adi"))

    print(front("Ad"))