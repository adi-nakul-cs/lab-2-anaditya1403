# Given two int values, return their sum. Unless the two values are the same, 
# then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a,b):
  if a!=b:
    return a + b
  else:
    return (a+b)*2

print(sum_double(3, 4))  # Output: 7
print(sum_double(3, 3))  # Output: 12
print(sum_double(3, 2))  # Output: 5
print(sum_double(1, 2))  # Output: 3
print(sum_double(5, 5))  # Output: 20
print(sum_double(0, 0))  # Output: 0
print(sum_double(0, 1))  # Output: 1