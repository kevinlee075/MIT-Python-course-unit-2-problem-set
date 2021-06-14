# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:10:54 2021

@author: Lenovo
"""

def Minimum_monthly_payment(balance, monthlyPaymentRate):
    '''
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    '''
    return balance * monthlyPaymentRate
def Monthly_unpaid_balance(balance, monthlyPaymentRate, mo):
    '''
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    '''
    if mo == 0:
        return balance * (1-monthlyPaymentRate)
    else:
        return (1-monthlyPaymentRate) * 