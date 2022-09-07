# String

# b l u e b e r r y    (string)
# 0 1 2 3 4 5 6 7 8    (index)

# Slicing example:

favorite_fruit = "blueberry"
last_char = favorite_fruit[len(favorite_fruit)-7]
print(last_char)

# or another way to write...

length = len(favorite_fruit)

last_chars = favorite_fruit[length-4:]

print(last_chars)

# If we wanted to find the last three letters of a string, we could use len:

last_three_letters = string_name[len(string_name)-3:]

# For Loops + Strings:

def print_each_letter(word):
  for letter in word:
    print(letter)

# For example: 

def get_length(word):
  count = 0
  for letter in word:
    count +=1
  print(count)

final_word_count = get_length("Sushi")

# Strings and Conditionals (Part One)

# Example1 Count

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

# Example2 True/False Boolean

def letter_check(word, letter):
  if letter in word:
    return True
  else:
    return False

checked_letter = letter_check("strawberry", "a")
print(checked_letter)

# Pythonic "In" and "Not In"
'''
There’s an even easier way than iterating through the entire string to determine if a character is in a string. We can do this type of check more efficiently using in. in checks if one string is part of another string.

Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

Solution example:
'''
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if letter in string_two and letter not in common:
        common.append(letter)
  return common

'''
String Summary:

A string is a list of characters.
A character can be selected from a string using its index string_name[index]. These indices start at 0.
A ‘slice’ can be selected from a string. These can be between two indices or can be open-ended, selecting all of the string from a point.
Strings can be concatenated to make larger strings.
len() can be used to determine the number of characters in a string.
Strings can be iterated through using for loops.
Iterating through strings opens up a huge potential for applications, especially when combined with conditional statements.

\n Newline
\t Horizontal Tab
Newline or \n will allow us to split a multi-line string by line breaks and \t will allow us to split a string by tabs. \t is particularly useful when dealing with certain datasets because it is not uncommon for data points to be separated by tabs.

Splitting this string at the escape sequence "\n", or newline, will produce a list of each line in the poem.
'''

# String Methods:

# Joining strings

'delimiter'.join(list_you_want_to_join)

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'

'''
Now this may seem a little weird, because with .split() the argument was the delimiter, but now the argument is the list. This is because join is still a string method, which means it has to act on a string. The string .join() acts on is the delimiter you want to join with, therefore the list you want to join has to be the argument.
'''

# Strip()
# Python provides a great method for cleaning strings: .strip(). Stripping a string removes all whitespace characters from the beginning and end.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append (line.strip()) #loop through all lines and stripping them of white space, then add each line to the new Stripped list that has no excess white space.
print(love_maybe_lines_stripped)

# Replace()
string_name.replace(character_being_replaced, new_character)
# Real example:
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer') #replacing Toomer with the word Tomer in Toomer_Bio

# Find()

# You can also search for larger strings, and .find() will return the index value of the first character of that string.

# Find searches a string for its argument returns the index location of that argument.

print("smooth".find('oo'))
# => '2'


# Example: 
god_wills_it_line_one = "The very earth will disown you"
disown_placement = (god_wills_it_line_one.find("disown"))


'''
Format Strings

The Python string method .format() replaces empty brace ({}) placeholders in the string with its arguments.
If keywords are specified within the placeholders, they are replaced with the corresponding named arguments to the method.
msg1 = 'Fred scored {} out of {} points.'
msg1.format(3, 10)
# => 'Fred scored 3 out of 10 points.'
 
msg2 = 'Fred {verb} a {adjective} {noun}.'
msg2.format(adjective='fluffy', verb='tickled', noun='hamster')
# => 'Fred tickled a fluffy hamster.'
'''
