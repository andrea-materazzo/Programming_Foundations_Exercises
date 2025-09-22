# Programming Exercise: Compound Interest Calculator
#
# Task: Write a program that calculates the ending principal in a bank
# account after compounding the interest.
#
# Requirements:
# 1. Ask the user to enter the starting principal
# 2. Ask the user to enter the annual interest rate (as a percentage)
# 3. Ask the user how many times per year the interest is compounded
# 4. Ask the user for how many years the account will earn interest
# 5. Calculate the ending balance using the compound interest formula:
#    A = P(1 + r/n)^(nt)
#    Where: A = ending amount, P = principal (startingAmount), r = annual interest rate (interestrate),
#           n = number of times interest is compounded per year, t = time in years
# 6. Display the ending balance formatted as currency
#
# Formula: a = p * (1 + r/n)^(n*t)
# Note: Remember to convert the interest rate from percentage to decimal
#
# Example output: "At the end of 5 years you will have $1,276.28"

startingAmount = float(input("Enter your starting capital"))
interestRate = float(input("Enter your interest rate in percent"))
timesCompounded = int(input("Enter the times the interest rate is compounded"))
durationOfInvestment = int(input("Enter the amount of years of the investment"))

totalAmount = startingAmount * (1 + (interestRate/100)/timesCompounded)**(timesCompounded*durationOfInvestment)
print(f"The total amount after {durationOfInvestment} years, with an interest rate of {interestRate}%, compounded {timesCompounded} times, is {totalAmount:,.2f} CHF")