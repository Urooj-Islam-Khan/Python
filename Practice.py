# 1.	 Write a program which prompts a user for a Fahrenheit  tempreture, convert the tempreture to Celsius and print out the converted tempreture.
# C = (f-32*5)/9
"""
Ftemp = float(input("Input Temp in Fahrenheit: "))
Ctemp = (Ftemp - 32) * 5 / 9
print("Temp in Celsius is: ", Ctemp)
"""

# 2.	Write a programs that input two numbers from the user, and  number raised to the power of the second number.
"""
num1, num2 = int(input("Enter 1st Number")), int(input("Enter 1st Number"))
print(num1, " raised to power of ", num2, "is: ", (num1**num2))
"""

# 3.	 Write a program that initialize two variables with integer (int) values and convert their data types to floating-point  (float), and displays them
"""

age = 19
weight = 50

print(age)
print(weight)

age = float(age)
weight = float(weight)

print(age)
print(weight)
"""

# 4.	Write a program to print the sum of two numbers.

"""
num1 = 20
num2 = 30

sum = num1 + num2
print("sum of ", num1, "and ", num2, "is: ", sum)
"""


# 5.	Write a program to print the first 10 natural numbers using while loop.

"""
t = 1
while t <= 10:
    print(t)
    t = t + 1

"""
# 6.	Write a pay computation program that prompts the user for ‘hours worked’ and ‘rate per hour’ and computes the gross pay. Your program should compute the pay by giving the employee 3.5 times the regular rate for the hours worked above 30 hour.
"""

hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))

gross_pay = 0.0
if hours <= 30:
    gross_pay = hours * rate
else:
    overtime = hours - 30
    gross_pay = hours * rate + rate * overtime * 3.5

print(gross_pay)
"""

# 7.	 Write a program that uses for loop to compute the average of numbers in a given list.
# [3.5, 6.4,9.4,0.5.1.2,2.5]
"""

list =  [3.5, 6.4,9.4,0.5,1.2,2.5]
sum = 0
for num in list:
    sum = sum+num

length = len(list)

print("Average of the given list is: ", (sum/length))
"""
# 8.	 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 0.1, print a grade according to these rules:
"""

try:
    score = float(input("Enter score between 0.0 and 1.0"))
    grade = ""

    if score <= 1.0 and score >= 0.9:
        grade = "A"
    elif score < 9.0 and score >= 0.8:
        grade = "B"
    elif score < 8.0 and score >= 0.7:
        grade = "B"
    elif score < 7.0 and score >= 0.6:
        grade = "B"
    else:
        grade = "Bad Score"
    print(grade)
except:
    print("Bad Score")
"""


# 9.	Use For loop to print number from 20 to 30.
"""

num = 20
for i in range(20, 31, +1):
    print(i)
"""


# 10.	Write a program to take the user's height and weight as input and calculate their BMI.
# BMI = weight / height**2

"""

height = int(input("Enter you Height"))
weight = input("Enter you weight")

BMI = weight / height**2
print(BMI)
"""

# 11.	Write a function that takes a list of numbers as input and uses a for loop to find the sum of numbers in the given list.
# list = [1, 2, 3, 4, 5, 6]
"""
def sum_of_list(sum_list):
    sum = 0
    for num in sum_list:
        sum = num + sum
    return sum

list = [1, 2, 3, 4, 5, 6]
print("Sum of list is: ", sum_of_list(list))
"""

# hw = "hello world"
# print(hw.title())
# print(hw.upper())
# print(hw.isdigit())
# print(hw.islower())

# 12.	 Write a program that uses a loop to find the Largest and smallest number in a given list of numbers.
"""
list = [3.5, 6.4, 9.4, 0.5, 1.2, 2.5]
largest = list[0]

smallest = list[0]

for var in list:
    if var > largest:
        largest = var

print("Largest: ", largest)

for var in list:
    if var < smallest:
        smallest = var

print("Smallest: ", smallest)
"""

# 13.	Write a program to calculate the length of a given message. Note: In this case do this WITHOUT using the built-in len() function.
"""

message = "Hello, I am Urooj Islam Khan"
count = 0
for letter in message:
    count = count + 1
print(count)

"""
# 14.	Write a program to calculate the length of a given message. 
# Note: In this case do this with using the built-in len() function.
"""message = "Hello, I am Urooj Islam Khan"

print(message.len())
"""
message = "Hello I am Urooj Islam Khan"

split = message.split()
print(split)

wordcount = 0

for var in split:
    wordcount = wordcount + 1

print(wordcount)

char_list = ['y', 'e', 'l', 'l', 'o', 'w']

word =  "" .join(char_list)

