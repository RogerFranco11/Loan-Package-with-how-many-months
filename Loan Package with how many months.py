# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:48:48 2023

@author: rjfch


Pmt = r * PV/(1-(1+r)**-n)
Pmt is how much you pay back/mo
n is number of months
r is interest rate per month 


"""

import numpy as np

def Idunno(PV, r, n):
    """
    Parameters 
    ----------
    PV : TYPE Float
    DESCRIPTION, Present value (amt borrow)
    r : TYPE Float 
    DESCRIPTION, Interest rate per month as a decimal
    n: TYPE Integer
    DESCRIPTION, Number of months to pay back loan 
    
    Returns
    -------
    Pmt : TYPE Float
    DESCRIPTION, amt paid per month 
    """
    Pmt = r * PV / (1 - (1 + r)**(-n))
    return Pmt

def calculate_num_months(PV, r, pmt):
    """
    Parameters
    ----------
    PV : TYPE Float
    DESCRIPTION, Present value (amt borrow)
    r : TYPE Float
    DESCRIPTION, Interest rate per month as a decimal
    pmt : TYPE Float
    DESCRIPTION, Monthly payment amount
    
    Returns
    -------
    n : TYPE Integer
    DESCRIPTION, Number of months to pay off the loan
    """
    n = np.log(1 - PV * r / pmt) / np.log(1 + r)
    return int(np.ceil(n))

# Input the PV
n = 48
PV = input('Enter PV: ')
PV = float(PV)

print(f"PV = {PV} \n")

r = input('Interest APR: ')
r = float(r) / 100
r = r / 12
print(f"Interest = {r:0.3f}")

pmt = Idunno(PV, r, n)
pmt = np.round(pmt, 2)
print(f"Payment is {pmt: } per month")

# Calculate the number of months to pay off the loan with the given payment
num_months = calculate_num_months(PV, r, pmt)
print(f"Number of months to pay off the loan: {num_months}")