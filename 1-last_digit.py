#!/usr/bin/python3
import random as rd
number = rd.randint(-10000,10000)

#Declarate last_digit variable with the last digit of number
last_digit = int(str(number)[-1])
#Do an if contiditional for values greater than 5
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))

#Do an elif conditional for zero value
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
#Do an else conditional for values less than 6 an not 0
else:
    print("Last digit of {} is {} and is less than 6 and is not 0".format(number, last_digit))
