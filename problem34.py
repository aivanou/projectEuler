import math

def digs(n):
    d = list()
    while n!=0:
        d.append(n%10)
        n/=10
    return d

cache = {}

def fact(n):
    if n==1:
        return 1
    if n==0:
        return 1
    if n==2:
        return 2
    if n in cache:
        return cache[n]
    ans = n*fact(n-1)
    cache[n]=ans
    return ans

def find():
    sm = 0
    i=3
    for i in range(3,11231000):
        s = sum([fact(d) for d in digs(i)])
        if s==i:
            sm+=i
            print i,sm

    print sm

if __name__ == '__main__':
    find()