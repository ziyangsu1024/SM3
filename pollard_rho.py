from gmpy2 import invert,gcd
import time
from functools import reduce
from random import randint,seed
import math

def quick_pow(x, y, p): #素性检测
    ans = 1
    while y:
        if y & 1:
            ans = ans * x % p
        x = x * x % p
        y >>= 1
    return ans

def miller_rabin(n, test_time = 8):
    if n < 3:
        return n == 2
    u = n - 1
    t = 0
    while u % 2 == 0:
        u //= 2
        t += 1
    for i in range(1, test_time + 1):
        x = randint(2, n - 1)
        v = quick_pow(x, u, n)
        if v == 1 or v == n - 1:
            continue
        for j in range(t + 1):
            v = v * v % n
            if v == n - 1:
                break
        else:
            return False
    return True

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
