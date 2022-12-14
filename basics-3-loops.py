'''
For Loop

In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length. With for loops, on each iteration, we will be able to perform an action on each element of the collection.

For Loops structure:

for <temporary variable> in <collection>:
  <action>

Example:
for game in board_games:
  print(game)

In a “for loop” you’re going through a list or tuple.
In a “while loop” it’s more generic, you have an arbitrary condition (i) that you check every time.

for i in moon_count:
print(moon_count[i])

Meaning: 
A for keyword indicates the start of a for loop.
A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
An in keyword separates the temporary variable from the collection used for iteration.
A <collection> to loop over. In our examples, we will be using a list.
An <action> to do anything on each iteration of the loop

'''

'''
For Loops: Using Range

Often we won’t be iterating through a specific list (or any collection), but rather only want to perform a certain action multiple times.

To create arbitrary collections of any length, we can pair our for loops with the trusty Python built-in function range().

The range() function can be used to create a list that can be used to specify the number of iterations in a for loop.
'''

for i in range(6):
  print(i)
  
# will print 0, 1, 2, 3, 4, 5

'''
If we are curious about which loop iteration (step) we are on, we can use temp to track it. Since our range starts at 0, we will add + 1 to our temp to represent how many iterations (steps) our loop takes more accurately.
'''

# Real life example of for loop using to skip from 91 to 100 in increments of 3.

  list = []
  i = start
  while i <= 100:
    lst.append(i)
    i += 3
  return lst

#Uncomment the line below when your function is done
print(every_three_nums(91))

'''

While Loops (Another type of loop):

In Python, a while loop will repeatedly execute a code block as long as a condition evaluates to True.

The condition of a while loop is always checked first before the block of code runs. If the condition is not met initially, then the code block will never run.

We know that while loops require some form of a variable to track the condition of the loop to start and stop.

General Structure:

while <conditional statement>:
  <action>
'''


# Examples of While Loops:

# This loop will only run 1 time
hungry = True
while hungry:
  print("Time to eat!")
  hungry = False
 
# This loop will run 5 times
i = 1
while i < 6:
  print(i)
  i = i + 1

# Another example of while loops:

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

length = len(ingredients)
index = 0
 
while index < length:
  print(ingredients[index])
  index += 1

# On the first iteration, we will be comparing the equivalent of 0 < 5 which will evaluate to True, and start the execution of our loop body.
# Increment index to access the next element in ingredients
# Each iteration gets closer to making the conditional no longer true

# Elegant Loops in Python vs Normal Versions:

# Normal version:

while count <= 3:
  print(count)
  count += 1

# Python allows us to write elegant one-line while loops: 

while count <= 3: print(count); count += 1

# For Loops [normal version]

numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)

# For Loops [Elegant]

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

#Template:
new_list = [<expression> for <element> in <collection>]

# Conditionals with Elegant List Comprehensions:

# List Comprehensions are very flexible. We even can expand our examples to incorporate conditional logic.

# For Loops [normal version] Conditional

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled) 


# For Loops [Elegant]:

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

# Same output for both numbers would be [-2, -90]. You can also use If-Else along with If.


# For Loop vs While Loop:

# Basic While Loop Example:

i = 1
while i < 11:
  print(i)
  i += 1

# Basic For Loop Example:

for i in range(1, 11):
  print(i)

# Loops to Countdown: 

countdown = 10
print("STARTING COUNTDOWN!")
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")

# Example of Loops through List
while index < length:
  print("I am learning about " + (python_topics[index]))
  index += 1
  
'''
Control Statements

Breaking Loops:

The Python Break statement can be used to terminate the execution of a loop. It can only appear within a for or while loop. It allows us to break out of the nearest enclosing loop. If the loop has an else clause, then the code block associated with it will not be executed if we use the break statement.

The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

If the break statement is inside a nested loop (loop inside another loop), the break statement will terminate the innermost loop.

'''

# Continue Loops:

# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for drinking_age in ages:
  if drinking_age < 21: (#this means if your drinking age is LESS than 21 that you should stop. Otherwise do continue.)
    continue
  print(drinking_age)

# the continue statement it simply moved to the next iteration of the list and thus never reached the print statement.

'''
Prints out...ages
38
34
26
21
67
41

Nested Loops:

In Python, loops can be nested inside other loops. Nested loops can be used to access items of lists which are inside other lists. The item selected from the outer loop can be used as the list for the inner loop to iterate over.
'''

groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]
 
# This outer loop will iterate over each list in the groups list 

for group in groups:

  # This inner loop will go through each name in each list

  for name in group:
   
 print(name)

# Example:

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for sales in location:
    scoops_sold += sales     
 #this one is a more elegant way of writing item1 + item2 = item2
#adding all the numbers from all the lists from scoops_sold
print(scoops_sold)

'''    
Python List Comprehension

Python list comprehensions provide a concise way for creating lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses: 

[EXPRESSION for ITEM in LIST <if CONDITIONAL>].

The expressions can be anything - any kind of object can go into a list.

A list comprehension always returns a list.

'''
# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]

print(result)
# [0, 4, 16, 36, 64]
    
    

# List Comprehensions: Elegant List Loops

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)

# Or

new_prices = [price - 5 for price in prices]
print(new_prices)

# Explanation of the example above:

# Re-examine the general structure of a list comprehension:

new_list = [<expression> for <element> in <collection>]


# A list comprehension always returns a list.

'''
In our case:

The <expression> will be our formula using our grade variable plus ten extra points: grade + 10


<element> can be any name you want. Since each element represents a grade, it makes sense to call it grade


Our <collection> is the list we want to loop through: grades


Is the same (and more elegant way of writing this: 
'''
    
numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)
    
'''

List Comprehensions: Conditionals

Conditionals are like ‘if, else, and elifs’

So in this example, these are heights and if you’re taller than 161 you can ride a cool roller coaster! To run through the list of shorties, you do a conditional loop.
'''
    
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

