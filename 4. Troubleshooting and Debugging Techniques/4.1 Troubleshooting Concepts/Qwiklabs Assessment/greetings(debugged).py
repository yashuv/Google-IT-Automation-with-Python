#!/usr/bin/env python3

import random

def greeting():
    name = input("Hello!, What's your name?")
    number = random.randint(1,101)
    # Debugged the issue (we have turned the number into a string using str() function.)
    print("hello " + name + ", your random number is " + str(number))

greeting()

'''
Conclusion:
We successfully debugged the colleague's python script. We reproduced the error, found its root cause, and applied the remediation to the issue. 
'''