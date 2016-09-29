import math

def sieve(n):
    s = []
    for i in range(1,n+1):
        s.append(True)
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

def rotate(n):
    d = ndigs(n)
    res = n%10
    n=n/10
    n+=(powTen(d-1)*res)
    return n

def isCircular(num,sieve):
    d = ndigs(num)
    for i in range(0,d):
        # print 'checking:',num
        if sieve[num]==False:
            return False
        num = rotate(num)
    return True

def find():
    n = 1000000-1
    nd = 0
    s=sieve(n*9)
    # print isCircular(197,s)
    for i in range(2,n+1):
        if isCircular(i,s):
            nd+=1
            print i,nd
    print nd

if __name__ == '__main__':
    find()