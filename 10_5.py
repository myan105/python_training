# Write a function called is_sorted that takes a list as a parameter and
# returns True if the list is sorted in ascending order and False otherwise.


def is_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

# Test cases
print(is_sorted([1, 2, 3, 4, 5]))     # True (sorted)
print(is_sorted([5, 4, 3, 2, 1]))     # False (not sorted)
print(is_sorted([1, 3, 2, 4, 5]))     # False (not sorted)
print(is_sorted(["apple", "banana", "cherry"]))  # True (sorted alphabetically)
print(is_sorted(["banana", "apple", "cherry"]))  # False (not sorted alphabetically)
