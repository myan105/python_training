#A number, a, is a power of b if it is divisible by b and 
#a/b is a power of b. Write a function called is_power that takes parameters 
#a and b and returns 
#True if a is a power of b. Note: you will have to think about the base case.

def is_power(a, b):
    if a == b:
        return True
    if a < b or a % b != 0:
        return False
    return is_power(a // b, b)

# Test cases
print(is_power(16, 2))  # True (16 is 2^4)
print(is_power(27, 3))  # True (27 is 3^3)
print(is_power(25, 5))  # True (25 is 5^2)
print(is_power(12, 3))  # False (12 is not a power of 3)
