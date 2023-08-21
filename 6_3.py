
def first(word):
    return word[0]

#Write a function called is_palindrome that takes a string argument and returns True 
#if it is a palindrome and False otherwise.
#Remember that you can use the built-in function len to check the length of a string.

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))
    
print(is_palindrome("noon"))
#Output : True