'''
SELF

Self is the strength of writing object-oriented programs. We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.
Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.

This convenience is most apparent when the constructor creates the instance variables, using the arguments passed in to it.
'''
      
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.url)
# prints "www.codecademy.com"
 
print(wikipedia.url)
# prints "www.wikipedia.org"
      
# Example:
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url
 
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.secure())
# prints "https://www.codecademy.com"
 
print(wikipedia.secure())
# prints "https://www.wikipedia.org"
      
# Class is useful because we are encapsulating data with operations on that data.

# Another example:
   
class Circle:
  pi = 3.14
 
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2
 
  def circumference(self): #already defined circumference
    return 2 * self.pi * self.radius  #so just return it.
#self.radius is above = diameter / 2.
 
medium_pizza = Circle(12) #define 3 circles.
teaching_table = Circle(36)
round_room = Circle(11460)
 
print(medium_pizza.circumference()) #Instance.Variable
print(teaching_table.circumference())
print(round_room.circumference())

'''
      
'''
Object’s Attributes:
We can use the dir() function to investigate an object’s attributes at runtime. dir() is short for directory and offers an organized presentation of object attributes.
'''
fake_dict = FakeDict()
fake_dict.attribute = "Cool"
 
dir(fake_dict)
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__()', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']
 
# all these duner methods are built ins of class.
# Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually indicated by double-underscores. But sure enough, attribute is in that list.

# String Rep... __repr()__
# Another dunder method called __repr__(). This is a method we can use to tell Python what we want the string representation of the class to be. __repr__() can only have one parameter, self, and must return a string.
  
class Employee():
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"
# without __repr__ it would have printed the memory location instead

# We implemented the __repr__() method and had it return the .name attribute of the object. When we printed the object out it simply printed the .name of the object! Cool!
      
# Another example:
def __repr__(self):
  return "Circle with radius {radius}".format(radius=self.radius)
    


'''
Class 1 Chapter Review:

What is… __init__ a function defined in a class, gives instructions on what to assign to a new instance when it’s created. Called a constructor __init__ gives object construction directions

What is… self What is the first argument of a method? = The instance of the object itself. We usually refer to it as self. self is not enforced by Python but is best practice to refer to it.

What is...type(): Type returns the class that an object implements.

__repr__ returns the string representation of an object.
'''
class Student: #CLASS
  def __init__ (self, name, year): #CONSTRUCTOR
    self.name = name  #ATTRIBUTE
    self.year = year #ATTRIBUTE
    self.grades = [] #ATTRIBUTE
    self.attendance = {}
  
  
  def add_grade(self, grade): #METHOD
    if type(grade) == Grade:
      self.grades.append(grade) #destination.append(thing_that_will_be_added)
  
  def get_average(self): #METHOD
    total = 0
    for grade in self.grades:
      total += grade.score
    average = total / len(self.grades)
    return average
 
  def mark_attendance(self, date, was_present):
    self.attendance[date] = was_present
 
 
class Grade: #CLASS
  minimum_passing = 65 #ATTRIBUTE (Class Variable...same thingy different words)
  
  
  def __init__(self, score): #CONSTRUCTOR
    self.score = score #Interalizes the score, so you don't have to track scores, they know their own store.
  
  
  def is_passing(self): #METHOD
    if self.score >= Grade.minimum_passing: # a period (.) is a connector it bridges the gap between an object and its reference.
      return True
    else:
      return False
 
 
#INSTANCE VARIABLES: What's special about car, baby, cake...we have a blueprint but the instance variable is what makes it special/customized.
roger = Student("Roger van der Weyden", 10) 
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(22))
pieter.mark_attendance('2021-08-01', True)
pieter.mark_attendance('2021-08-02', False)
pieter.mark_attendance('2021-08-03', True)
print(pieter.attendance)

'''
Types of Class Variables in Python:
Inside a class, we can have three types of variables. They are:
1. Instance variables (object level variables)
2. Static variables (class level variables)
3. Local variables
'''
