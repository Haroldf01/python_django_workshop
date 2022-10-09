# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary with dict() method
_dict = dict({1: 'python', 2: 'it', 3:'is'})
print(_dict)

# Creating a Dictionary with each item as a Pair
_dictionary = dict([
    (1, 'Devansh'),
    (2, 'Sharma')
])
print("\nDictionary with each item as a pair: ")
print(_dictionary)

# Accessing the dictionary values
# the values can be accessed in the dictionary by using the keys as keys are unique in the dictionary

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print("Name : %s" %Employee["Name"])
print("Age : %d" %Employee["Age"])
print("Salary : %d" %Employee["salary"])
print("Company : %s" %Employee["Company"])

new_dictionary = {}
print("Empty Dictionary: ")
print(new_dictionary)

# Adding elements to dictionary one at a time
new_dictionary[0] = 'Peter'
new_dictionary[2] = 'Joseph'
new_dictionary[3] = 'Ricky'
print("\nDictionary after adding 3 elements: ")
print(new_dictionary)

# Adding set of values with a single Key
new_dictionary['Emp_ages'] = 20, 33, 24
print(new_dictionary)

print("Deleting some of the employee data")
del Employee["Name"]
del Employee["Company"]

# Deleting a key using pop() method
pop_ele = new_dictionary.pop(3)

###########
## dictionary methods
###########
print('\nall_values - {}'.format(Employee.values()))
print('\nall_keys - {}'.format(Employee.keys()))

print('\nget method - {}'.format(Employee.get('Name')))

inventory = {'shirts': 25, 'paints': 220, 'shocks': 525, 'tshirts': 217}
print('\npop - {}'.format(inventory.pop('shirts')))
print('\npopitem - {}\n'.format(inventory.popitem()))
