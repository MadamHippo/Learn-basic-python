'''
CLASSES!

As an analogy, a class can be thought of as a blueprint (Car), and an instance is an actual implementation of the blueprint (Ferrari).

Python Types

five = 5
print(type(five))
#prints out <class ‘int’>


Above, we defined two variables, and checked the type of these two variables.

A variable’s type determines what you can do with it and how you can use it. You can’t .get() something from an integer, just as you can’t add two dictionaries together using +. This is because those operations are defined at the type level.

A class is a template for a data type. Defining a class means capitalizing the names of classes to make them easier to identify.
'''

# Instantiation

# A class doesn’t accomplish anything simply by being defined. A class must be instantiated. In other words, we must create an instance of the class, in order to breathe life into the schematic.

# Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined class as follows:

class Facade:
  pass

facade_1 = Facade()

# Instantiation takes a class and turns it into an object, the type() function does the opposite of that. When called with an object, it returns the class that the object is an instance of.

print(type(facade_1)
#prints <class '__main__.Facade'>
      
'''
We then print out the type() of facade_1 and it shows us that this object is of type __main__.facade_1

...why does this matter?
Because a class instance is also called an object. 

The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.

Instantiation takes a class and turns it into an object, the type() function does the opposite of that.

Class Variables
When we want the same data to be available to every instance of a class we use a class variable. 

A class variable is a variable that’s the same for every instance of the class.

You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.

'''
class Musician:
 title = "Rockstar"
 
drummer = Musician()
print(drummer.title)
# prints "Rockstar"

'''
Above we defined the class Musician, then instantiated drummer to be an object of type Musician. We then printed out the drummer’s .title attribute, which is a class variable that we defined as the string “Rockstar”.

If we defined another musician, like guitarist = Musician() they would have the same .title attribute.

Here’s another example:
'''
class Grade:
  minimum_passing = 65 #Class Variable...it's a variable that defines a specific attribute or property for a class and may be referred to as a member variable or static member variable.
passing_grade = Grade()
print(passing_grade.minimum_passing)
#prints out 65
 
highest_score = Grade()
print(highest_score.perfect_score)
#prints 100

# In Python, class variables are defined outside of all methods and have the same value for every instance of the class.

# Class variables are accessed with the instance.variable or class_name.variable syntaxes.
      
class my_class:
  class_variable = "I am a Class Variable!"
  
x = my_class()
y = my_class()
 
print(x.class_variable) #I am a Class Variable!
print(y.class_variable) #I am a Class Variable!
 
#basically the same exact example as above with grade()



