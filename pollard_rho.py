from gmpy2 import invert,gcd
import time
from functools import reduce
from random import randint,seed
import math
def Pollard_RHO(p, c): #pollard_rho 算法
    (i,k)=(1,2)
    x=randint(0,p)
    y=x
    while 1:
        i+=1
        x=(x*x%p+c)%p
        d=gcd(y-x,p)
        if d!=1 and d!=p:
            return d
        if y==x:
            return p
        if i==k:
            y=x
            k+=k
def PrimeFactorsListGenerator(p): #利用 pollard_rho 算法进行整数分解
    result = []
    if p <= 1:
        return None
    if miller_rabin(p): #先素性检测
        return [p]
    n=p
    while n>=p:
        n = Pollard_RHO(n, randint(1, p - 1))
    result.extend(PrimeFactorsListGenerator(n))
    result.extend(PrimeFactorsListGenerator(p // n))
    return result
