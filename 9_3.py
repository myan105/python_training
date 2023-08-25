#Write a function named avoids that takes a word and a string of forbidden letters, 
#and that returns True if the word doesn’t use any of the forbidden letters.

def avoids(word, forbidden_letters):
    for letter in word:
        if letter in forbidden_letters:
            return False
    return True
# Test cases
print(avoids("hello", "abc"))  # True 
print(avoids("apple", "xyz"))  # False