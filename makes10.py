# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True


#we define a function including 2 arguments a and b.
# so if a=10 *or* b=10 *or* a + b = 10
# it returns True
# else False


def makes10(a,b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    
    else:
        return False
    
if __name__ == "__main__":
    print(makes10(4,6))

    print(makes10(10,20))

    print(makes10(36,10))

    print(makes10(-20,30))

    print(makes10(6,3))

    print(makes10(40,-30))

    print(makes10(9,0))