import math


def sieve(n):
    s = []
    for i in range(1,n+1):
        s.append(True)
    s[0]=False
    s[1]=False
    for i in range(2,int(math.sqrt(float(n)))):
        if s[i]==False:
            continue
        j = i*i
        while j<len(s):
            s[j]=False
            j+=i
    return s

def ndigs(n):
    if n==0:
        return 0
    return 1+ndigs(n/10)

def powTen(n):
    if n==0:
        return 1
    return 10*powTen(n-1) 

def trunkLeft(n):
    return n%powTen(ndigs(n)-1)

def trunkRight(n):
    return n/10

def isTruncatable(n,s,func):
    while n!=0:
        if s[n]==False:
            return False
        n = func(n)
    return True

def isTruncatablePrime(n,s):
    return isTruncatable(n,s,trunkLeft) and isTruncatable(n,s,trunkRight)


def find():
    n = 90000000
    s = sieve(n)
    sm =0 
    for i in range(11,n):
        if isTruncatablePrime(i,s):
            sm+=i
            print i,sm
    print sm

if __name__ == '__main__':
    find()