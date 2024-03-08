# Write Python code to print the numbers in the list given below after removing even numbers from it.
"""
num_list = [3, 1, 18, 4, 11, 10, 6, 20]
out_list = []
for i in num_list:
    if i % 2 != 0:
        out_list.append(i)
print(out_list)
"""


"""
# Rewrite the above Python code, using list comprehension method, to print the numbers in the list given below after removing even numbers from it.
num_list = [3, 1, 18, 4, 11, 10, 6, 20]
num_list = [3, 1, 18, 4, 11, 10, 6, 20]


outlist = [i for i in num_list if (i%2!=0]
print(outlist)
"""


# 3: Write Python code that takes a list of nums and displays the product of all numbers in the lsit.
"""
num_list = [3, 1, 18, 4, 11, 10, 6, 20]

a = 1

for i in num_list:
    a = a * i

print(a)
"""

# 4. Write python code to do the following, using the list given below:
# get the smallest number
# get the largest number
# get the size or length of the list
# get the sum of all numbers in the list
"""
num_list = [3, 1, 18, 4, 11, 10, 6, 20]


print(min(num_list))
print(max(num_list))
print(len(num_list))
print(sum(num_list))

"""
# 5. Write Python code to take a list of characters and convert it into a single word 'yellow'.

"""char_list = ["y", "e", "l", "l", "o", "w"]
word = "".join(char_list)
print(word)
"""

# 6.Write Python code that takes the two list given below, and joins them to create a new list, sort the new list and display it
"""
list1 = [3, 1, 18, 4]
list2 = [11, 10, 6, 20]

# Expected output:
# list1 = [3, 1, 18, 4]
# list2 = [11, 10, 6, 20]
# new_list = [1, 3, 4, 6, 10, 11, 18, 20]

new_list = list1 + list2
new_list.sort()
print(new_list)
"""

# Write a program to calculate the length of a given message.
"""
name = "hussain"
a = 0
for i in name:
    a = a + 1

print(a)
"""

# Take the following Python code that stores a string:
str_val = "X-DSPAM-Confidence:0.8475"
# Use find() function and string slicing to extract the portion of the string after the colon  character and then use the float() function to convert the extracted string into a floating point number. Verify by checking the type of the converted number

"""
find = str_val.find(":")
print(find)

colon_pos = str_val[find + 1 :]
print(colon_pos)

con_float = float(colon_pos)

"""
# Consider the string give below, and the write python code to do the followig tasks:
str_val = "the quick brown fox jumps over the lazy dog"
# 1. Print the slice of first 10 characters
# 2. Print the slice of last 10 characters
# 3. Replace the with a in the given string

# print(str_val[0:10])


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

my_str = "     hello    "
print(my_str)  # <------
print(my_str.lstrip())  # remove whitespace from the left
print(my_str.rstrip())  # remove whitespace from the right
print(my_str.strip())  # remove trailing whitespace from both sides
