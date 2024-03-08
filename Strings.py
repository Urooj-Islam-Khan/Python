# Create a String              we can use both " "  & ' '
name = "Urooj"
Roll_no = "2k22/SWE/124"

# To print a string use print()
print(name)
print(Roll_no)

# For multiline String we can use ''' '''
Address = """ Street no:4, House no:4/217 Sarfaraz Colony 
            near Police line"""

print(Address)

# To find the length off a string we can use len() function
length_of_name = len(name)
print(length_of_name)  # find length of a string by making variable

print(len(Roll_no))  # Direct finding length of a string

# Concanate two strings by using + sign
greeting = "Hello"
print(greeting + name)

# Repetition using * operator
a = "abc \n" * 10
print(a)

# indexing a string by putting position of that number in [ ]
print(greeting[0])  # greeting index 0
# or to print last Index
print(greeting[-1])

# We can use a : to perform *slicing* which grabs everything up to a designated point.
a = "Hello World"
print(a[:3])
# it will print Hel

print(a[3:])
# it will print lo World

print(a[-3:])
# it will print rld
# Grab everything but the last letter
print(a[:-1])

# Grab everything, but go in steps size of 1
print(a[::2])

# it will print HloWrd  it means print 1st letter then skip 2nd then print thi3rdd and so on

str = "Urooj"
# to convert string in uppercase
print(str.upper())

# to convert string in lowercase
print(str.lower())


# to find type of variable
print(type(str))

# to check is it numeric
print("124".isnumeric())  # True

# to check is it uppercase
str.upper().isupper()

# we can use the rstrip(), lstrip(), strip() methods of str
my_str = "     hello    "
print(my_str)  # <------
print(my_str.lstrip())  # remove whitespace from the left
print(my_str.rstrip())  # remove whitespace from the right
print(my_str.strip())  # remove trailing whitespace from both sides

# to replace a word
my_str = "This is the car"
print(my_str.replace("the", "a"))
print(my_str.replace("r", "t"))

s = "the quick brown fox jumps over the lazy dog"
# Split a string by blank space (this is the default)
print(s)
print("Split: ", s.split())

# it'll print ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print("Join")
print("-".join(s))

# it will print  'the-quick-brown-fox-jumps-over-the-lazy-dog'


# to find
print(name.find("r"))

age = 28
# print("age = ", (age))
print("age = {}".format(age))
