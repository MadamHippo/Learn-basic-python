'''
Dictionary

A dictionary is an unordered set of key: value pairs.

It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated with one another.

Notice that:
A dictionary begins and ends with curly braces { and }.
Each item consists of a key ("avocado toast") and a value (6).
Each key:value pair is separated by a comma.
Lists cannot be the keys of a dictionary, because they are mutable
To add a single key: value pair to a dictionary, we can use the syntax:

'''
dictionary[key] = value

menu["cheesecake"] = 8

# Another example: 

dictionary_name[key] = value

final_dictionary[word] = (len(word))

'''
Add / Merge Dictionary{} Multiple Keys

If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.
'''
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

# Overwrite Values

# In that case, our value assignment would overwrite the existing value attached to the key 'avocado toast'.

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

menu["oatmeal"] = 5

'''
Dictionary List Comprehensions:

Python allows you to create a dictionary using a list comprehension, with this syntax:
'''
new_dict = {key:value for key, value in zip(key_list, value_list)}

'''
Accessing Dictionary Key

Once you have a dictionary, you can access the values in it by providing the key. 

If the key already exists, the old value will be overwritten if you use the assignment operator again.

Attempting to access value with a key that doesn’t exist is a keyerror.

Example format: 
'''
print(zodiac_elements["fire"])

'''
Checking if Item in Key

One way to avoid this error is to first check if the key exists in the dictionary:
'''
key_to_check = "Landmark 81"
 
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

# This will not throw an error, because key_to_check in building_heights will return False, and so we never try to access the key.

# Try/Except Keys

  key_to_check = "Landmark 81"
  try:
    print(building_heights[key_to_check])
  except KeyError:
    print("That key doesn't exist!")



