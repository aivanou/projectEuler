import math


def sieve(n):
    s = []
    primes = []
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
    return primes


def isPermutation(v1, v2):
    return sorted(v1) == sorted(v2)

def nextPerm(v):
    

def find():
    primes = sieve(10000)
    used = [False] * 10000

if __name__ == '__main__':
    find()
    # print computeNum(2,2)
