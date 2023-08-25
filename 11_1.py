#Write a function that reads the words in words.txt and
# stores them as keys in a dictionary. It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to
# check whether a string is in the dictionary.

def create_word_dictionary(filename):
    word_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            word_dict[word] = None
    return word_dict

filename = "words.txt"
word_dictionary = create_word_dictionary(filename)

# Check if a word is in the dictionary
word_to_check = "hello"
if word_to_check in word_dictionary:
    print(f"{word_to_check} is in the dictionary.")
else:
    print(f"{word_to_check} is not in the dictionary.")
