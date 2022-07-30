from Crypto.Util.number import long_to_bytes,isPrime
from functools import reduce
from gmpy2 import gcd,invert,iroot
from math import gcd
import time
start = time.perf_counter()
#Shanks's Babystep-Giantstep Algorithm

class node:
    def _init_(self):
        self.vue=0
        self.num=0
def cmp(a):
      return a.vue
def init_list(first,g,n,p):
      List=[]
      temp=node()
      temp.vue,temp.num=first,0
      List.append(temp)
      for i in range(1,n+1):
            temp=node()
            temp.num = i
            temp.vue = List[i-1].vue * g % p
            List.append(temp)
      List.sort(key=cmp)
      return List
def sDLP(a,b,p):
    ans=p
    n=iroot(p,2)[0]+1
    L1=init_list(1,a,n,p)
    aa=pow(invert(a,p),n,p)
    L2=init_list(b,aa,n,p)
    i = 0
    j = 0
    while True :
        if (i>=n or j>=n): break
        while (L1[i].vue < L2[j].vue and i<n): i += 1
        while (L1[i].vue > L2[j].vue and j<n): j += 1
        if L1[i].vue == L2[j].vue :
            x=L1[i].num+L2[j].num*n
            return int(x)


#通过调用 Factor(n) 进行质因数分解，返回值是因数列表。

def f(x):
    return x**2 + 1

def pollard_rho(N):
    xn = 2
    x2n = 2
    d = 1
    while d == 1:
        xn = f(xn) % N
        x2n = f(f(x2n)) % N
        abs_val = abs(xn - x2n)
        d = gcd(abs_val, N)
    return d

def Factor(n):       #返回一个因式列表
    ans=[]
    while True:
        temp=pollard_rho(n)
        ans.append(temp)
        n=n//temp
        if n==1:return ans
        if isPrime(n):
            ans.append(n)
            return ans
n = int(input("p= "))
print(Factor(n))
