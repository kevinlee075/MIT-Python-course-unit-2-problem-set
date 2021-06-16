# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:10:54 2021

@author: Lenovo
"""

balance = int(input('balance = ')) #type the initial balance
monthlyPaymentRate = float(input('monthlyPaymentRate = ')) #type the minimal monthly rate
annualInterestRate = float(input('annualInterestRate = ')) #type the annual interest rate
def Remaining_balance_1(balance, monthlyPaymentRate, annualInterestRate):
    '''
    Unpaid balance = b0 - b0*mP = b0 * (1-mP)
    I0 = aP/12 * unpaid balance = b0 * (1-mP) * aP/12
    Remaining balance at the first month = balance * (1-mP) * (1+aP)
    Using similar strategy, I found remaining balance at the n month \
        = balance * (1-mP)^n * (1+aP/12)^n
    therefore, remaining balance at the 12th month = balance * (1-mP)^12 * (1+aP/12)
    '''
    n = 1 
    while n <= 12: #using while looping to multiply (1-mP)*(1+P/12) 12 times
        balance *= (1-monthlyPaymentRate) * (1+annualInterestRate/12)
        n += 1
    Rb = round(balance, 2) #following the problem set requirement, we need to round our results at the 0.01 place
    return Rb #return our function
ans = Remaining_balance_1(balance, monthlyPaymentRate, annualInterestRate)
print('Remaining balance: ', str(ans)) #print the remaining balance


def total_balance(balance, annualInterestRate):
    '''
    Total balance = balance * (1+aP/12)^12
    '''
    o = 1
    while o <= 12:
        balance *= (1+annualInterestRate/12)
        o += 1
    total_balance = balance
    return total_balance
def payoff_inteterest(annualInterestRate, p):
    '''
    The first payoff will have the compounding interest p-1 times, the second one\
        will have p-2 times, ..., and the final one will not have interest
    '''
    POI = 0
    if p == 1:
        return 1
    else:
        POI = (1 + annualInterestRate/12) ** (p-1)
        return POI + payoff_inteterest(annualInterestRate, p-1)
fixed_monthly_payment = total_balance(balance, annualInterestRate) // payoff_inteterest(annualInterestRate, 12)
if fixed_monthly_payment < 10.0:
    print('Lowest Payment: ' + str(10))
else:
    fixed_monthly_payment = round(fixed_monthly_payment, -1)
    print('Lowest Payment: ' + str(fixed_monthly_payment))
    
    
initial_balance = int(input('balance = ')) #type the initial balance
annualInterestRate = float(input('annualInterestRate = ')) #type the annual interest rate
balance = initial_balance
upperbound = balance/12.0
lowerbound = (balance * (1 + (annualInterestRate/12) ** 12))/12.0
payment = (upperbound + lowerbound)/2
def monthlyinterest():
    '''
    monthly interest = unpaid balance * monthly interest rate
    '''
    return (balance - payment) * (annualInterestRate/12)
while balance > 0:
    for mo in range(12):
        balance = balance - payment + monthlyinterest()
    if balance < 0:
        upperbound = payment
        balance = initial_balance
    elif balance > 0:
        lowerbound = payment
        balance = initial_balance
    else:
        break
    payment = (upperbound + lowerbound)/2
print('lowest interest: ' + str(payment))

