#Write a function named uses_only that takes a word and a string of letters, and that returns 
#True if the word contains only letters in the list.

def use_only(word, available):
    for letter in word:
        if letter not in available:
            return False
        return True
