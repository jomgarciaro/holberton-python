#!/usr/bin/python3
for i in range(1, 100):
    if i < 10:
        print("{:02.0f}, ".format(i), end='')
        continue
    elif i == 89:
        print("{}".format(i))
        break
    elif str(i)[0] < str(i)[1]:
        print("{}, ".format(i), end='')
        continue
