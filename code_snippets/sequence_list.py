L1 = ["John", 102, "USA"]


list_ = [1,2,3,4,5,6,7]
print(list[0])
print(list[1])

# Slicing the elements
print(list[0:6])

# By default the index value is 0 so its starts from the 0th element and go for index -1.
print(list[:])
print(list[2:5])
print(list[1:6:2])

###########
## list operators
###########

print('\nlist concat = {}\n'.format(L1 + list_))
print('\nlist repetition = {}\n'.format(L1 * 2))

###########
## list methods
###########

new_list = list(range(1, 6))
print('\ndefault list - {}\n'.format(new_list))

# add element to the end of the list
new_list.append("this is a string and new element")
print('\nadd element - {}\n'.format(new_list))

# remove elements from the list
new_list.remove(2)
print('\nremove element - {}\n'.format(new_list))
new_list.pop()
print('\nremove last element - {}\n'.format(new_list))

# sort the list
new_list.sort()
print('\nsort the list - {}\n'.format(new_list))

# remove all elements from the list
new_list.clear()
print('\nempty the list - {}\n'.format(new_list))
