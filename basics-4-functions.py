'''
Functions:

Functions are simplified sections of code we can reuse. Easier to read. Functions have names (although some languages use placeholders for short functions.)

Parameter vs Arguments

To summarize, here is a quick breakdown of the distinction between a parameter and an argument:

The parameter is the name defined in the parenthesis of the function and can be used in the function body.

'''

def trip_welcome(destination): #destination = parameter
  print("Hi welcome to" + destination + "!")
 
# The argument is the data that is passed in when we call the function and assigned to the parameter name.
trip_welcome("Empire State Building") #Empire State Building is argument.

'''
Types of Arguments

Positional arguments: arguments that can be called by their position in the function definition.
'''
Example: 

def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )
# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)

'''
Keyword arguments: arguments that can be called by their name. A keyword argument is just a positional argument with a default value. 

Alternatively, we can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the function call. Notice in the code example below that the arguments do not follow the same order as defined in the function declaration.
'''

calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

# Default arguments: arguments that are given default values.

	calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

# When using a default argument, we can either choose to call the function without providing a value for a discount (and thus our function will use the default value assigned) or overwrite the default argument by providing our own:


# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)



# Built-in Functions: example...

length_of_destination = len(destination_name)


# Function Returns: example...

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

# Functions with multiple returns....

# A function that returns multiple values would like like this:

my_function():
  a = 1
  b = 2
  c = 3
  return a, b, c

'''
Scope and Nested Functions

Nested functions provide a great example of how scope is determined in our program. Typically, the order of scope follows the pattern where inner functions are able to access outer function variables, but outer functions are not able to access inner function variables.
'''


'''
Real World Exercises: (If Elif Else Statements With Functions) 

Define the function to accept five parameters starting with budget then food_bill, electricity_bill, internet_bill, and rent
Calculate the sum of the last four parameters
Use if and else statements to test if the budget is less than the sum of the calculated sum from the previous step.
If the condition is true, return True otherwise return False

# Write your over_budget function here:
'''
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False

print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True
'''
Similarly to the last problem, we can perform the operations within the condition of the if statement to prevent us from creating an extra variable. We calculate the sum and compare it to budget at the same time and return True if the condition is met, otherwise we return False.
'''

# List Comprehension vs For Loop

flights = ["1122", "5533", "9992"]

code_a = ["BA" + flight for flight in flights]
print(code_a)

# vs...
code_b = []
for flight in flights:
  code = "BA" + flight
  codes_b.append(code)
print(codes_b)

'''
An example of real world problem (using loops and elif/else statments with functions):
Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. To do this, we will need the following steps:

Define our function to accept a single input parameter lst which is a list of numbers
Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
Within the loop, if the first number in the list is even, then remove the first number of the list
Once we hit an odd number or we run out of numbers, return the modified list

Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!

Hint
Use a while loop to check two things. First, check if the list has at least one element, using len(lst). Second, check to see if the first element is odd using mod (%). If both of those are True, slice off the first element of the list using lst = lst[1:].


#Write your function here

(Original Way to Solve it Using Len & While Loop)

def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst

This ^ is reducing the size of the list

After defining our method, we use a while loop to keep iterating as long as some provided conditions are true. We provide two conditions for the while loop to continue. We will keep iterating as long as there is at least one number left in the list len(lst) > 0 and if the first element in the list is even lst[0] % 2 == 0. If both of these conditions are true, then we replace the list with every element except for the first one using lst[1:]. Once the list is empty or we hit an odd number, the while loop terminates and we return the modified list.

(Different While Loop Style of Answering Q)
  i = 0
  while i < len(lst):
    if lst[i] % 2 == 1:
      return lst[i:]
    i += 1
  return []

^ this is using a pointer and incrementing pointer

(Using For Loop)

  new_list = []
  found_odd = False
  for num in lst:
    if num % 2 == 1:
      new_list.append(num)
      found_odd = True
    elif found_odd:
      new_list.append(num)
  return new_list



#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
'''
