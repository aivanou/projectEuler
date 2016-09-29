import time
import math


# def phi(n):
#     res = n
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#                 while n % i == 0:
#                     n /= i
#                 res -= res / i
#             i += 1
#         if n > 1:
#             res -= res / n
#     return res

# print phi(2930)


def even(num):
    return num & 1 == 0


def mulmod(a, b, n):
    if a > n:
        a %= n
    if b > n:
        b %= n
    res = 0
    while b != 0:
        if not even(b):
            res += a
            while res >= n:
                res -= n
            b -= 1
        else:
            a = a << 1
            while a >= n:
                a -= n
            b = b >> 1
    return res


def powMod(a, b, n):
    res = 1
    while b != 0:
        if not even(b):
            res = mulmod(res, a, n)
            b -= 1
        else:
            a = mulmod(a, a, n)
            b = b >> 1
    return res


# decomposes number to the q*2^p
def decompose(num):
    p, q = 0, 0
    while even(num):
        p += 1
        num = num >> 1
    return p, num


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def isPrime(n):
    start, rounds = 7, 1
    for i in range(0, rounds):
        if not millerRabinTest(n, start):
            return False
        start += 1
        while gcd(n, start) != 1:
            start += 1
    return True


def millerRabinTest(n, b):
    if n <= 3 or even(n):
        return False
    (p, q) = decompose(n - 1)
    res = powMod(b, q, n)
    if res == 1 or res == n - 1:
        return True
    for i in range(0, p):
        res = mulmod(res, res, n)
        if res == n - 1:
            return True
    return False


def sq_root(num):
    return math.floor(math.sqrt(num))


def ferma(n):
    x, y = int(sq_root(n)), 0
    r = x * x - n
    while True:
        # print r, x, y
        if r == 0:
            return x - y if x != y else x + y
        else:
            if r > 0:
                r -= y + y + 1
                y += 1
            else:
                r += x + x + 1
                x += 1


def factorization(n):
    def test():
        return 1
    return test()


def trivialIsPrime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
# print ferma(10)


def multMatr(p1, p2):
    res = [[], []]
    for i in range(0, 2):
        for j in range(0, 2):
            res[i].append(0)
    for i in range(0, len(p1)):
        for j in range(0, len(p2)):
            for k in range(0, len(p2)):
                res[i][j] += p1[i][k] * p2[k][j]
    return res


def matrPow(p, n):
    res = p
    n -= 1
    while n != 0:
        if even(n):
            p = multMatr(p, p)
            n = n >> 1
        else:
            res = multMatr(res, p)
            n -= 1
    return res


def fib(n):
    p = [[0, 1], [1, 1]]
    pn = matrPow(p, n)
    return pn[0][1]


def trivialFib(n):
    f1, f2 = 0, 1
    while n != 0:
        f = f1 + f2
        f1 = f2
        f2 = f
        n -= 1
    return f2


def p(n):
    return n * (3 * n - 1) / 2


def t(n):
    return n * (n + 1) / 2


def h(n):
    n * (2 * n - 1)

combs=[]

def maxForTh(tarr, th, marr, ind, csum, sm):
    if len(tarr)==ind:
        if sm!=csum:
            return
        if th>=0:
            combs.append(list(marr))
        return
    marr.append(tarr[ind])
    sm+=marr[-1]
    maxForTh(tarr,th,marr,ind+1,csum, sm)
    sm-=marr[-1]
    marr.pop()
    marr.append(tarr[ind]+th)
    sm+=marr[-1]
    maxForTh(tarr,th,marr,ind+1,csum, sm)
    sm-=marr[-1]
    marr.pop()
    marr.append(tarr[ind]-th)
    sm+=marr[-1]
    maxForTh(tarr,th,marr,ind+1,csum, sm)
    sm-=marr[-1]
    marr.pop()


maxForTh([56,43,12,32],4,[],0,sum([56,43,12,32]),0)
for c in combs:
    print c
