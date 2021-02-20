#!/usr/bin/python3
def uppercase(str):
#    for i in range(len(str) - 1):
#        print("{}".format(chr(ord(str[i]) - 32) if (ord(str[i]) in range(97, 123)) else str[i], end='')
#    print("{}".format(chr(ord(str[-1]) - 32) if (ord(str[-1]) in range(97, 123)) else str[-1]))
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
            print(i, end='')
        else:
            print(i)
