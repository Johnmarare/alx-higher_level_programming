#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        print("{:d}{:d}".format(num1, num2),
              end='\n' if num1 == 8 and num1 + 1 == 9 else ', ')
