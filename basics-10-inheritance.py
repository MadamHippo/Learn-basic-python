# INHERITANCE AND POLYMORPHISM
# Interfaces
# When two classes have the same method names and attributes, we say they implement the same interface. An interface in Python usually refers to the names of the methods and the arguments they take. Other programming languages have more rigid definitions of what an interface is, but it usually hinges on the fact that different objects from different classes can perform the same operation (even if it is implemented differently for each class).
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * 0.001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * 0.00005
 
# Polymorphism
# Polymorphism is the term used to describe the same syntax (like the + operator here, but it could be a method name) doing different actions depending on the type of data.
# For an int and an int, + returns an int
2 + 4 == 6

# For a float and a float, + returns a float
3.1 + 2.1 == 5.2

# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"

# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]
 
# In this example we use the dunder method __ add __

class Atom:
  def __init__(self, label):
    self.label = label
    
  def __add__(self, other):
    return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
            self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine
 
# Mode dunder methods available:
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
    
  def __len__(self):
    return len(self.lawyers)
  
  def __contains__(self, lawyer):
    return lawyer in self.lawyers
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

# Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:

names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}

# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.
# So in example above, the function would return:
{"S" : 4, "L": 3}



# Write your count_first_letter function here:
 
def count_first_letter(names):
  first_letter_names = {} #Empty list
  for name in names: #Looping thru the dict of names
    first_letter = name[0] #Accessing the dict's key (last name's first letter)
    if first_letter not in first_letter_names: # If key's last name's first letter isn't inside first_letter_names (the empty list) then...
      first_letter_names[first_letter] = 0 # make it equal zero or none.
    first_letter_names[first_letter] += len(names[name]) # Adding the first letter from the list and seeing how many values (names) from the dict matches the letter with it's own first letter. 
  
  return first_letter_names
 
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
