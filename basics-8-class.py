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

'''
Methods

Methods are functions that are defined as part of a class. 
The first argument in a method is always the object that is calling the method. We name this first argument self
We define methods similarly to functions, except that they are indented to be part of the class.
'''
      
class Dog:
  dog_time_dilation = 7
 
  def time_explanation(self): # <- method
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))
 
pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

# Above we created a Dog class with a time_explanation method that takes one argument, self, which refers to the object calling the function. We created a Dog named pipi_pitbull and called the .time_explanation() method on our new object for Pipi.

# Notice we didn’t pass any arguments when we called .time_explanation(), but were able to refer to self in the function body. When you call a method it automatically passes the object calling the method as the first argument.

'''
Methods in Classes with Arguments

Methods always have at least this one argument.
_Methods_ are _functions_ that can be called on instances of a class. They are a more specific name for a _function_ and are called using parentheses `()`. If we have a variable that contains an object instance, we can call methods on that instance as `instance_var.operation_name()`, where `instance_var` is the variable holding an instance, and `operation_name` is the name of the method we want to use. The `()` are required to tell Python to run the operation, and is used to provide any needed arguments.

'''
      
# Dog class
class Dog:
  # Method of the class
  def bark(self):
    print("Ham-Ham")
# Create a new instance
charlie = Dog()
 
# Call the method
charlie.bark()
# This will output "Ham-Ham"
 
print(charlie.bark())
      
# We define methods similarly to functions, except that they are indented to be part of the class.

