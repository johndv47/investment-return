'''
script: investment_return.py
action: a. request user input for investment time horizion.
        b. perform interest calculation.
        c. print calculation.
author: John Pinto
date: 1/16/2026
'''

n = int(input("Enter the number of years: "))
r = 0.07
p = 1000
a = p * (1+r)**n
print(a)
