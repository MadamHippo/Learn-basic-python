'''
CS 101 Path Codecademy...



LIST INDICES

Python list elements are ordered by index, a number referring to their placement in the list. List indices start at 0 and increment by one.

~ remove() delete the matching element/object whereas del and pop removes the element at a specific index.
~ del and pop deals with the index. The only difference between the two is that- pop return deleted the value from the list and del does not return anything.
~ Pop is the only way that returns the object.
~ Remove is the only one that searches objects (not index).

~ If you want to delete a specific object in the list, use remove method.
~ If you want to delete the object at a specific location (index) in the list, you can either use del or pop.
~ Use the pop, if you want to delete and get the object at the specific location

Which list would be created by running this code?

list(range(2, 14, 4))
2 = where you start.
14 = where you should stop before.
4 = how much you actually need to skip between.
[2 , 6, 10 is the answer]

'''

# LISTS IN PYTHON
'''
In Python, lists are a versatile data type that can contain multiple different data types within the same square brackets. The possible data types within a list include numbers, strings, other objects, and even other lists.
'''

# Adding Lists Together
items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

# List Methods:
# append()
orders = ['daisies', 'periwinkle']
orders.append('tulips')
print(orders)
# Result: ['daisies', 'periwinkle', 'tulips']

# remove()

# count()
#We use the count() function to find the number of occurrences for each item.

#If we want to know how many times i appears in this word, we can use the list method called .count():

backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')

print(numPen)
# Output: 3

# List Negative Indices:
soups = ['minestrone', 'lentil', 'pho', 'laksa']
soups[-1]   # 'laksa'
soups[-3:]  # 'lentil', 'pho', 'laksa'
soups[:-2]  # 'minestrone', 'lentil'

# Modifying & Accessing 2D Lists
# A 2D list of names and hobbies
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# The sublist of Jenny is at index 0. The hobby is at index 1 of the sublist. 
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)

# Insert()
'''
It takes in two inputs:

The index that you want to insert into.
The element that you want to insert at the specified index.
'''
# Zip()
'''
Zip () 

The zip() function allow us to combine two lists into an iterator of tuples with the list elements paired together.
The zip() function takes two (or more) lists as inputs and returns an object that contains a list of pairs.

'''
# Dict Comprehensions with Zips:
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

'''
Takes a pair from the iterator of tuples
Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
Creates a key : value item in the students dictionary
Repeats steps 1-3 for the entire iterator of pairs

'''
# Convert Zip from Memory:

# An iterator of pairs between name list and height list:

names_and_heights = zip(names, heights)

print(names_and_heights)

# Would output: <zip object at 0x7f1631e86b48>

# This zip object contains the location of this variable in our computer’s memory.

# In order to print zip list, use List()
converted_list = list(names_and_heights)
print(converted_list)

# Pop()
# Len()
# Sort()
# Note: The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. If we do assign the result of the method, it would assign the value of None to the variable.
'''
The Python sorted() function accepts a list as an argument, and will return a new, sorted list containing the same elements as the original.
Sorted does not modify the original, unsorted list.

The sorted() function is different from the .sort() method in two ways:

It comes before a list, instead of after as all built-in functions do.
It generates a new list rather than modifying the one that already exists.

'''

# Output
# [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# 2D list of people's heights
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
# Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)

'''
List Slicing

If we want to select the first n (n=number) elements of a list, we could use the following code:

fruits[:n] (take the firsts)

fruits[n:] (take anything but the firsts)

To get an element of a list, use the syntax list[n], where n is the index of the item you want to get. 

Remember that list indices start at zero!

We can do something similar when we want to slice the last n elements in a list:

fruits[-n:] (take the lasts)

Negative indices can also accomplish taking all but n last elements of a list.

fruits[:-n] (all but last)

Which of the following code selects the last three elements of mylist?
fruits[-3:]
We can use negative indexes to count backwards from the last element in a list.

'''

# Bonus: Lambda in python to sort lists

'''
How to sort a list of lists by the fourth element in each list?

pizza_and_prices.sort(key=lambda x: x[1])

key=lambda x: x[1]) #lambda in python is an inline anonymous function and in this case it returns the second element of the list (so you can access prices in nested list below)

Example: pizza_and_prices = [["pepperoni", 2], ["pineapple", 6], ["cheese", 1], ["sausage", 3], ["olives", 2], ["anchovies", 7], ["mushrooms", 2]]


'''
