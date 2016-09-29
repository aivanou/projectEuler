import math 

def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

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

def toNum(digs):
    num =0
    for dig in digs:
        num=num*10+dig
    return num

def perms(digs,cnum,maxNum,sieve):
    if len(digs)==maxNum:
        if isPrime(toNum(digs))==True:
            return toNum(digs)
        return -1
    mx = -1
    for i in range(1,maxNum+1):
        if i in digs:
            continue
        digs.append(i)
        cr = perms(digs,i+1,maxNum,sieve)
        mx = max(mx,cr)
        digs.pop()
    return mx

def fperms(n,sieve):
    print(perms([],1,n,sieve))

def find():
    s = sieve(133)
    fperms(7,s)

if __name__ == '__main__':
    find()