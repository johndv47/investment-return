'''
script: investment_return.py
action: a. loops through years 10, 20, and 30 to perform interest calculation.
        b. prints calculation.
note: p(1+r)^n
      p = principal
      r = rate
      n = years
author: John Pinto
date: 1/19/2026
'''
print("Welcome to the investment return calculator!\n")

years = [10, 20, 30]
r = 0.07
p = 1000

for n in years:
    a = p * (1+r)**n
    print(f"After {n} years, your principal amount (${p}), will be ${a:.2f}.")
