"""
Written by Ivan Debono
ivandebono [at] idebono [dot] eu


23 April 2017

PURPOSE Output the Copeland-Erdős constant up to desired nth prime
        (See http://mathworld.wolfram.com/Copeland-ErdosConstant.html)

INPUT   n: position of last prime (e.g. last=10 means up to 10th prime)

OUTPUT  copeland_erdos_str: string representation of Copeland-Erdős constant
        copeland_erdos: Copeland-Erdős constant, in Python Decimal format
        (i.e. floating point with any user-defined precision),
        to same number of primes as n
"""    

from decimal import getcontext, Decimal 
import numpy as np
import sympy

def copelanderdos(n): 

    # First generate list of primes up to n
    primes=[]
    for prime in np.arange(1,n+1): primes.append(sympy.ntheory.generate.prime(prime))

    copeland_erdos_str='0.'+''.join(str(p) for p in primes)    
    getcontext().prec = len(copeland_erdos_str)
    copeland_erdos_flt=Decimal(copeland_erdos_str)

    return copeland_erdos_str,copeland_erdos_flt



"""
Written by Ivan Debono
ivandebono [at] idebono [dot] eu

October 2016
Modified 22 April 2017

PURPOSE Output the Champernowne constant up to desired digit
        (See http://mathworld.wolfram.com/ChampernowneConstant.html)

INPUT   last: last digit
        base: base representation for digit. Default = 10

OUTPUT  champernowne_str: string representation of Champernowne's constant
        champernowne_flt: Champernowne's constant, in Python Decimal format
        (i.e. floating point with any user-defined precision),
        to same number of digits as last digit
"""    

from decimal import getcontext, Decimal 
import numpy

def champernowne(last,base=10): 

    champernowne_str = "0."
    for c in range(1,last+1):
        champernowne_str += str(numpy.base_repr(c,base=base))
    getcontext().prec = len(champernowne_str)
    champernowne_flt=Decimal(champernowne_str)
    return champernowne_str,champernowne_flt
