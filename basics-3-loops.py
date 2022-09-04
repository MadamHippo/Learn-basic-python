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

