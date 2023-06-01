#!/usr/bin/env python3

import random

def greeting():
    name = input("Hello!, What's your name?")
    number = random.randint(1,101)
    print("hello " + name + ", your random number is " + number)

greeting()

# We can reproduce the error by running the file in cwd using the following command:
# python greetings(error).py

## So, according to error we can conclude that the root cause of the issue is within the print statement, which is trying to concatenate two different data types (i.e., string and int).

# we debugged the issue in the another debugged python file