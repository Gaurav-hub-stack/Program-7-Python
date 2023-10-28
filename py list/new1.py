################## List ######################
# Creating an empty list
x = []
print(type(x), x)

# Creating a list with various elements
x = [10, 15, 20, "hii", -5, 6.7, True, [1, 5]]
print(type(x), x)

# Accessing elements in the list
print(x[0])
print(x[::-1])

# Numeric operations on a list
m1 = 700
m2 = 500
m3 = 625
x = [m1, m2, m3, 650, 890, 700]
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
print(sum(x) / len(x))
print(sorted(x))  # Returns a new list in ascending order (quick sort)
print(sorted(x, reverse=True))

# Appending values to the list
x = [10, 20]
print(x)
x.append(5)
x.append([3, 6])  # Added as a sub-list
print(x)

# Inserting a value at a specific index
x.insert(0, 100)

# Replacing a value at a specific index
x[2] = 16

# Searching in a list
x = [10, 20, 30]
print(20 in x)
print(200 in x)

# Removing elements from a list
x = [10, 20, 30, 40, 50, 10, 31, 53.0]

# Removing a specific value (only the first occurrence)
x.remove(10)

# To remove all occurrences of a given value
while 10 in x:
    x.remove(10)

# Removing by index
del x[0]  # Removes the value at the given index

# Removing and returning a value by index
v = x.pop(0)

# Removing the last value and returning it
v = x.pop()

# Clearing the list (removing all values)
x.clear()

# List Concatenation
x = [10, 20]
y = [1, 2, 3]
z = x + y
print(z)

############### tuple
# Creating a tuple using parentheses
my_tuple = (1, 2, 'apple', 3.14)

# Creating a tuple using commas (with or without parentheses)
another_tuple = 5, 'banana', 3.14159

# A tuple with a single element (note the trailing comma)
single_element_tuple = (42,)

#############SET

my_set = {1, 2, 3, 4, 5}
another_set = set([1, 2, 2, 3, 3, 4, 4, 5, 5])
# This will result in a set with unique elements {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
# Removes the element 3 from the set

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)  # Intersection
union = set1.union(set2)  # Union
difference = set1.difference(set2)  # Set difference


##### interview Question
# Creating a list using user input
x = []
for i in range(3):
    v = int(input("Enter value: "))
    x.append(v)
print(x)

# Creating a list using a string
x = list("bharat")
print(x)

# Creating a list using range()
x = list(range(1, 11))
print(x)

# Creating a list using list comprehension
x = [i * i for i in range(1, 5)]
print(x)

# Creating a list from user input using list comprehension
x = [int(input("Enter value: ")) for i in range(3)]
print(x)

# List comprehension with multiple loops
x = [i * j for i in range(1, 4) for j in range(2, 5)]
print(x)

# Creating a tuple
x = ()
print(type(x), x)

x = (10, 20, 10, 30)
print(x)
print(x[-1])

# Tuple example
x = (10, 20, 30, 40, 50)
print(len(x))
print(min(x))
print(max(x))
print(sum(x))

# Creating a tuple from a string
x = tuple("bharat")
print(x)

# Creating a tuple from range()
x = tuple(range(1, 10))
print(x)

# Creating a tuple from a list
x = tuple([1, 2, 3])
print(x)

# Creating a set
s = {10, 20, -5, 2.8, "hi"}
print(s)
for i in s:
    print(i)

s.add(52)
print(s)
s.remove(20)
print(s)

# Creating a set from a string
s = set("bharat")
print(s)

# Creating a set from range()
s = set(range(1, 5))

# Creating a set from a list
s = set([10, 20, 30, 40])
print(s)

# Creating a set from a tuple
s = set((10, 20, 30))
print(s)

s1 = {10, 20, 25, 63}
s2 = {30, 40, 50}

# Set operations
s3 = s1 | s2  # Union
print(s3)

s3 = s1 & s2  # Intersection
print(s3)

s5 = s1 - s2  # Difference
print(s5)
##############dict
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print(my_dict['name'])  # Accessing the value associated with the 'name' key

my_dict['age'] = 31  # Changing the value associated with the 'age' key
my_dict['country'] = 'USA'  # Adding a new key-value pair

del my_dict['city']  # Removing the 'city' key-value pair
my_dict.pop('age')  # Removing and returning the value associated with 'age'
for key, value in my_dict.items():
    print(key, value)

################### interview Assement
# Creating a dictionary
d = {
    101: "virat",
    105: "rohit",
    204: "rahul"
}
print(type(d))
print(d)

wc = {"bharat": ['rohit', 'gil', 'virat'], 'aus': ('warner', 'zampa')}
print(wc)

# Creating an empty dictionary
c = {}
print(type(c))

# Creating an empty set
s = set()
print(type(s))

d = {10: 'sachin', 18: 'kohli', 7: 'dhoni'}
print(d)

# Adding, updating, and accessing dictionary elements
d[63] = 'surya'  # Added to the dictionary
d[45] = 'sharma'  # If the key exists, updates its value
print(d)
print(d[7])  # Accessing the value of the key
del d[7]  # Deleting a key-value pair
print(d)
v = d.pop(1)  # Deleting a key-value pair and returning the value
print(d)
print(v)

k, v = d.popitem()  # Deleting the last key-value pair and returning both
print(d)
print(k, v)

# Dictionary length, minimum, maximum, and sorting
d = {10: 'sachin', 45: 'rohit', 7: 'dhoni'}
print(d)
print(len(d))
print(min(d))
print(max(d))
print(sorted(d))
print('sachin' in d)

# Iterating through a dictionary
for key in d:  # By default, iterates through keys
    print(key)

for value in d.values():
    print(value)

# Clearing the dictionary
d.clear()
print(d)

# Creating a dictionary from user input
d = {}
for i in range(3):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v
print(d)

# Creating a dictionary using dictionary comprehension
d = {i: i * i for i in range(1, 5)}
print(d)

d1 = {'a': "apple", 'b': 'ball'}
d2 = {'a': 'android', 'i': 'iphone'}

d1.update(d2)  # Merging dictionaries
print(d1)
