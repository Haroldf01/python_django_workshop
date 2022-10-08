# Creating an empty tuple
empty_tuple = ()
print("Empty tuple: ", empty_tuple)

# Creating tuple having integers
int_tuple = (4, 6, 8, 10, 12, 14)
print("Tuple with integers: ", int_tuple)

# Creating a tuple having objects of different data types
mixed_tuple = (4, "Python", 9.3)
print("Tuple with different data types: ", mixed_tuple)

# Creating a nested tuple
nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))
print("A nested tuple: ", nested_tuple)

# new tuple
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")

# Counting the occurrence of an element of the tuple using the count() method
print(tuple_.count('Ordered'))

# Getting the index of an element using the index() method
print(tuple_.index('Ordered'))
# This method returns index of the first occurrence of the element
