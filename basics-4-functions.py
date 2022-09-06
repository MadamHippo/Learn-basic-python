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

