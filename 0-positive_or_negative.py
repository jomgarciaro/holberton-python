#!/usr/bin/python3

import random
number = random.randint(-10,10)

#Do an "if" conditional for positive values
if number > 0:
    print(number, 'is positive')
#Do an elif conditional for zero value
elif number == 0:
    print(number, 'is zero')
#Do an else for negative values
else:
    print(number, 'is negative')
