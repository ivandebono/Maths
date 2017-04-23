"""
Written by Ivan Debono
ivandebono [at] idebono [dot] eu


23 April 2017

PURPOSE Output the Copeland-Erdős constant up to desired digit
        (See http://mathworld.wolfram.com/Copeland-ErdosConstant.html)

INPUT   last: last prime (e.g. last=10 means up to 10th prime)

OUTPUT  copeland_erdos_str: string representation of Copeland-Erdős constant
        copeland_erdos: Copeland-Erdős constant, in Python Decimal format
        (i.e. floating point with any user-defined precision),
        to same number of digits as last digit
"""    

from decimal import getcontext, Decimal 
import numpy as np
import sympy

def CopelandErdos(last): 

    # First generate list of primes up to last
    primes=[]
    for prime in np.arange(1,last+1): primes.append(sympy.ntheory.generate.prime(prime))

    copeland_erdos_str='0.'+''.join(str(p) for p in primes)    
    getcontext().prec = len(copeland_erdos_str)
    copeland_erdos_flt=Decimal(copeland_erdos_str)

    return copeland_erdos_str,copeland_erdos_flt

 