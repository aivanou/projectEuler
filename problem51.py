
import math

def sieve(n):
    s = []
    primes = list()
    for i in range(1, n + 1):
        s.append(True)
    for i in range(2, int(math.sqrt(float(n)))):
        if s[i] == False:
            continue
        primes.append(i)
        j = i * i
        while j < len(s):
            s[j] = False
            j += i
    for i in range(1,len(s)):
        if s[i]:
            primes.append(i)
    return (primes,s)


def relpace_all_digs(num,fr,to):
    return replace(num,get_digs_pos(num,fr),to)

def get_digs_pos(num, dig):
    pos=[]
    ind=0
    while num!=0:
        if num%10==dig:
            pos.append(ind)
        num/=10
        ind+=1
    return pos

def replace(num,pos,dig):
    for p in pos:
        num=replace_dig(num,p,dig)
    return num

def replace_dig(num,pos,dig):
    return num - pow(10,pos)*(get_dig(num,pos)-dig)

def get_dig(num,pos):
    ind=0
    while ind!=pos:
        num/=10
        ind+=1
    return num%10

def check_dig(primes, num, dig):
    count=0
    if len(get_digs_pos(num,dig))==0:
        return 0
    for d in range(dig+1,10):
        num1=relpace_all_digs(num,dig,d)
        if primes[num1]:
            count+=1
    return count+1

def has_fam(primes,prime):
    mx = 0
    for d in [0,1,2]:
        count = check_dig(primes,prime,d)
        if prime==56003:
            print d,count
        mx=max(count,mx)
    return mx

def compute(fam_size):
    (primes,s) = sieve(1000000)
    # print primes
    for prime in primes:
        count = has_fam(s, prime)
        if count>=fam_size:
            print prime
            return

if __name__ == '__main__':
    compute(8)


