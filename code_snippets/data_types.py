###########
## High level types
###########

a=10
b="Hi Python"
c = 10.5
print(type(a))
print(type(b))
print(type(c))


###########
## Numbers
###########

a = 5
print("The type of a", type(a))

b = 40.5
print("The type of b", type(b))

c = 1+3j
print("The type of c", type(c))
print(" c is a complex number", isinstance(1+3j,complex))

###########
## Sequence Types
###########

# String

str_var = "string using double quotes"
print(str_var)
s = '''A multiline
string'''
print(s)

# List

list1  = [1, "hi", "Python", 2]
# Checking type of given list
print(type(list1))

# Printing the list1
print (list1)

# List slicing
print (list1[3:])

# Tuple

tup  = ("hi", "Python", 2)
# Checking type of tup
print (type(tup))

#Printing the tuple
print (tup)

# Tuple slicing
print (tup[1:])
print (tup[0:1])

# Tuple concatenation using + operator
print (tup + tup)
