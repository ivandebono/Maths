"""
Written by Ivan Debono
ivandebono [at] idebono [dot] eu

October 2016
Modified April 2017

PURPOSE Output the Champernowne constant up to desired digit
        (See http://mathworld.wolfram.com/ChampernowneConstant.html)

INPUT   last: last digit

OUTPUT  champernowne_str: string representation of Champernowne's constant
        champernowne_flt: Champernowne's constant, in Python Decimal format
        (i.e. floating point with any user-defined precision),
        to same number of digits as last digit
"""    

from decimal import getcontext, Decimal  

def Champernowne(last): 
 
    champernowne_str = "0."
    for c in range(1,last+1):
        champernowne_str += str(c)
    getcontext().prec = len(champernowne_str)
    champernowne_flt=Decimal(champernowne_str)
    return champernowne_str,champernowne_flt