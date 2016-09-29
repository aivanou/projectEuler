import math

def isPal(s):
    (l,r) = (0,len(s)-1)
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

def find():
    n = 1000000
    sm = 0
    for i in range(1,n):
        if isPal(str(i)) and isPal(bin(i)[2:]):
            sm+=i
            print i,sm
    print sm

if __name__ == '__main__':
    find()