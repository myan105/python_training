#Write a function called has_no_e that returns True 
#if the given word doesn’t have the letter “e” in it.

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
print(has_no_e("hello"))

#output: False