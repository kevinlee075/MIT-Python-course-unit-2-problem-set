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
        balance *= (1-monthlyPaymentRate) * (1+annualInterestRate/12.0)
        n += 1
    Rb = round(balance, 2) #following the problem set requirement, we need to round our results at the 0.01 place
    return Rb #return our function
ans = Remaining_balance_1(balance, monthlyPaymentRate, annualInterestRate)
print('Remaining balance: ', str(ans)) #print the remaining balance


