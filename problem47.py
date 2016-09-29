import math


def sieve(MAX):
    primes = set()
    sv = [True] * (MAX + 1)
    for i in range(2, MAX + 1):
        if sv[i] == False:
            continue
        primes.add(i)
        j = i * i
        while j <= MAX:
            sv[j] = False
            j += i
    return primes


def factorize(num, primes):
    if num in primes:
        return set([num])
    ans = set()
    while num > 1:
        if num in primes:
            ans.add(num)
            break
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                ans.add(i)
                num /= i
                break

    return ans


def unique(s1, s2):
    if len(s1) != len(s2):
        return False
    for el in s1:
        if el in s2:
            return False
    return True


def solve(MAX):
    primes = sieve(MAX + 10)
    for i in range(1, MAX + 1):
        s1 = factorize(i, primes)
        s2 = factorize(i + 1, primes)
        s3 = factorize(i + 2, primes)
        s4 = factorize(i + 3, primes)
        if unique(s1, s2) and unique(s1, s3) and unique(s1, s4) and len(s1) == 4 and unique(s2,s3) and unique(s2,s4) and unique(s3,s4):
            print i,s1,s2,s3,s4
            print i

if __name__ == '__main__':
    solve(10000000)
