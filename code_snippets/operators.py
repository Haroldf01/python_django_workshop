a = 20
b = 10

# Arithmetic Operators
print('\naddition - {}\n'.format(a + b))
print('\nsubtraction - {}\n'.format(a - b))
print('\nmultiplication - {}\n'.format(a * b))
print('\ndivision - {}\n'.format(a / b))
print('\nmodulus - {}\n'.format(a % b))
print('\nexponent - {}\n'.format(a ** b))
print('\nfloor division - {}\n'.format(a // b))

# Assignment operators
a += b
print('\nplus equals - {}\n'.format(a))
a **= b
print('\nexponent equals - {}\n'.format(a))
print('\nvalue of B - {}\n'.format(b))

# identity operators
x = 90
y = 90
print(x is y)
print(a is b)

print(a is not b)
print(x is not y)
