'''
BASICS

What is a Variable? What is a Value?

~ A variable is nothing but a name that refers to a value. An assignment statement creates new variables and gives them values. The type of a variable means the type of the value it refers to.

~ Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

'''

# Adding Variable to String

# To add a variable to a string, you can use the syntax:

"My age is " + str(my_age) + "Another String"

# Note: You have to cast the number as a string before you add it to another string!


# += Macro Shortcut

# If you want to add 2 for each loop and 4 times, you could write it like this:

x = x + 2; x = x + 2; x = x + 2; x = x + 2;

# That’s a lot of work, right? So they invented a macro, a shortcut that means x = x + number. The shortcut uses the += operator:

x += 2



'''
How to create a basic list with range: 

The range() function can be used to create a list that can be used to specify the number of iterations in a for loop.
'''

my_list = list(range(1, 1001))

# Or

for i in range(len(hairstyles)): 
# triple wrapped up to get individual items out of a list
# Examples: 

# Print the numbers 0, 1, 2:
for i in range(3):
  print(i)
 
# Print "WARNING" 3 times:
for i in range(3):
  print("WARNING")

# Range() range statement. This will generate a list of numbers, and iterating through these will allow your for loop to execute the right number of times:

# Len(), which was a function that determined the number of characters in a string

'''
Reverse / Skip Range

However, you don’t want i to start at 0. Instead you want it to start at the last index of your string (len(my_string)-1) and end at 0.

Edit the call to the range function to do this. Remember, the range function can take three parameters: 
the starting number (inclusive),
the ending number (exclusive), 
and the step. To count down, make the step -1.

'''

# Reversing a String w/Range.

def reverse_string(word):
  reversed_word = ""
  for letters in range(len(word)-1, -1, -1):
reversed_word += word[letters]
return reversed_word

# Another example:

def reverse_string(input_str):
    answer = ""
    # Your code goes here
 
    for letter in range(len(input_str) - 1, -1, -1):
      answer += input_str[letter]
      print(answer)
 
    #  End of your code
    return answer

'''
Since the parameter for the ending index is exclusive we need to provide the index of one more iteration than what we want to stop at. 

We want to stop at 0, and since we are incrementing by -1, we will set the ending index to -1. 

Finally, make sure to add the third parameter of -1. This makes us increment by -1 at each step.

~ the first -1 is length of word minus 1. 
~ second -1 is the end. ( You stop before you hit -1)
~ third -1 is increment, you start at the end and you go down 1 everytime.
And you stop at -1 which stops you at 0.
'''


'''
Larger Sum

We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

Define the function to accept two input parameters: lst1 and lst2
Create two variables to record the two sums
Loop through the first list and add up all of the numbers
Loop through the second list and add up all of the numbers
Compare the first and second sum and return the list with the greater sum
'''

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num1 in lst1:
    sum1 += num1
  for num2 in lst2:
    sum2 += num2
  if sum1 >= sum2:
      return lst1
  else:
      return lst2
 
