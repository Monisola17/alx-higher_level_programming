#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

a = int(repr(number)[-1])

if a > 5:
    print(f"Last digit of {number :d} is {a} and is greater than 5")
elif a == 0:
    print(f"Last digit of {number :d} is {a} and 0")
else:
    print(f"Last digit of {number :d} is {a} and is less than 5")
