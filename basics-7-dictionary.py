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

# .Get() Keys 

# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default:

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# Things to Know About .Get(): The .get() function only returns the value associated with the key.
# There is no key 3 in this dictionary, so the default provided to the .get() function, ["hamburger", "fries"], will be printed.

'''
Delete a Key

We can use .pop() to do this. Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary. .pop() works to delete items from a dictionary, when you know the key value.
To pop a value from one dictionary and assign it to another, you can use syntax like:
 '''
new_dict["new key"] = old_dict.pop("old key")


# Get All Dict Keys

# Sometimes we want to operate on all of the keys in a dictionary. Like if you only wanted names of students “Grace, Jeffrey Sylvia etc.” you can use keys.

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

users_test_scores = test_scores.keys()

