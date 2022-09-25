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


# Another Complete Example w/ Personal Notes
      
class Circle: #this is a class. Class is a template that has variables and functions associated with it. It reduces code. A class must be instantiated, we must create an instance of the class, in order to breathe life into the schematic.
  pi = 3.14 #this is a variable. We're defining a class. 3.14 is a value. variables are used to store data related to the given class above.
  def area(self, radius): # area is Method with 2 arguments/objects. Self is a special parameter we use in methods to access the class variable right above. Without Self the variable is out of local scope. Self is implicitly passed.
    area = Circle.pi * radius ** 2 # Pi here is a class variable. You can access it as an Attribute of the class by using a . (period)
Attribute means regarding something being caused by something.
Radius ** 2 is a type of expression.
    return area  #you have to return a method.
 
circle = Circle() # Circle() creates an Instance. Similar to calling functions. The circle is a variable. A class instance is also called an object. () = I’m calling another piece of code, like an argument.
 
pizza_area = circle.area(12 / 2)  #We are accessing the class variable with .area(). The data held by an object is referred to as an Instance Variable or Instance Attribute. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to - in this case the object is 12 / 2 and the instance variable is area(). 
circle = Circle() the class and area is def as self, radius. Self is the Instance of class above. And dividing by 2 is because 12 (measurement of pizza) is the diameter instead of radius.
teaching_table_area = circle.area(36 / 2)
We're calling circle.area (instance.method) and using 36/2 as the argument.
When we want to create something from the class variable then that's called instances. To access a class variable we write the instance name and . [period] And then the variable we want.
round_room_area = circle.area(11460 / 2)
Print (instance.variable) #accessing a class variable. Class variables are accessed with the instance.variable or class_name.variable syntaxes.

      
'''
The Class Constructors

There are several methods that we can define in a Python class that have special behavior. These methods are sometimes called “magic,” because they behave differently from regular methods. Another popular term is dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

constructor __init__ gives object construction directions.

These are:
__init__() 
//This method is used to initialize a newly created object. It is called every time the class is instantiated.
Methods that are used to prepare an object being instantiated are called constructors. constructor in Python are usually talking about the __init__() method.
'''
class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"
      
'''
Above we created a class called Shouter and every time we create an instance of Shouter the program prints out a shout.
Shouter() looks a lot like a function call, doesn’t it? If it’s a function, can we pass parameters to it? We absolutely can, and those parameters will be received by the __init__() method.
'''
      
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
 
      # then shout it out
      print(phrase.upper())
 
shout1 = Shouter("shout")
# prints "SHOUT"
 
shout2 = Shouter("shout")
# prints "SHOUT"
 
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

'''
Above we’ve updated our Shouter class to take the additional parameter phrase. When we created each of our objects we passed an argument to the constructor. The constructor takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.
'''
      
      
'''
Class & instance variables

The data held by an object is referred to as an instance variable. 
Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.
We can instantiate two different objects from this class, fake_dict1 and fake_dict2, and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.
'''
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
 
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
 
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

'''
We’ve learned:
Class  is a schematic for a data  type.
Object is an instance of a class.
But why differentiate the 2 if each object must have methods + class variables the class already have??
Answer: because each instance of class holds different kinds of data.

Object oriented programming is bundling of related data and functionality. OOP grouping data and functionality inside an object, it's also called Encapsulation. In functional programming, functions and data are separate.

Class is a schematic for a data type.
Object is an instance of a class.
'''
 
'''
Objects = Instances

(A form of)...Method = Constructor

Super()__init__ sets the properties of instances.

Super() refers to the Parent class.

__init__ refers to the Person's conductor which will let us set the properties of the conductor...like name, age.

Then we can create objects like own property and inherit method from both parent and conductor.

A Getter method is actually an Accessor Method that returns the value of an instance variable. 

While a Setter method is also called a Mutator method. It is used to set the value of an instance variable in a Python class.
'''
      
'''
Attribute Functions

Instance variables and class variables are both attributes of an object.

What if we aren’t sure if an object has an attribute or not? 

hasattr() will return True if an object has a given attribute and False otherwise. 

hasattr() returns a boolean that evaluates whether the given object has the attribute given by the second argument.

If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute. 

The syntax and parameters for these functions look like this:
hasattr(object, “attribute”) has two parameters:
~object : the object we are testing to see if it has a certain attribute
~attribute : name of attribute we want to see if it exists

getattr(object, “attribute”, default) has three parameters (one of which is optional):
~object : the object whose attribute we want to evaluate
~attribute : name of attribute we want to evaluate
~default : the value that is returned if the attribute does not exist (note: this parameter is optional)
'''
      
# Example:
hasattr(attributeless, "fake_attribute")
# returns False
 
getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

'''
Above we checked if the attributeless object has the attribute fake_attribute. Since it does not, hasattr() returned False. After that, we used getattr to attempt to retrieve other_fake_attribute. Since other_fake_attribute isn’t a real attribute on attributeless, our call to getattr() returned the supplied default value 800, instead of throwing an AttributeError.
'''
