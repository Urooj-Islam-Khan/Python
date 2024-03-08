# 1.	 Write a program which prompts a user for a Fahrenheit  tempreture, convert the tempreture to Celsius and print out the converted tempreture.
# C = (f-32*5)/9

Ftemp = float(input("Input Temp in Fahrenheit: "))
Ctemp = (Ftemp - 32) * 5 / 9
print("Temp in Celsius is: ", Ctemp)
