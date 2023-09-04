#Write a definition for a class named Kangaroo with the following methods:
#1. An __init__ method that initializes an attribute named pouch_contents to an empty list.
#2. A method named put_in_pouch that takes an object of any type and adds it to
#pouch_contents.
#3. A __str__ method that returns a string representation of the Kangaroo object and the con-
#tents of the pouch.
#Test your code by creating two Kangaroo objects, assigning them to variables named kanga and
#roo, and then adding roo to the contents of kanga’s pouch.



class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        return f'Kangaroo object with pouch contents: {self.pouch_contents}'

# Test the code
kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch("joey")
kanga.put_in_pouch("wallet")
roo.put_in_pouch("key")
print(kanga)
print(roo)
