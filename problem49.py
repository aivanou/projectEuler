import math


def sieve(n):
    s = []
    primes = []
    for i in range(1, n + 1):
        s.append(True)
    for i in range(2, n):
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


def getAllPerms(num):
    perms = set()

    return perms


def nextPerm(v):
    lst = list(str(v))
    i1 = -1
    for i in range(0, len(lst) - 1):
        if lst[len(lst) - 2 - i] < lst[len(lst) - 1 - i]:
            i1 = len(lst) - 2 - i
            break
    if i1 == -1:
        return -1
    i2 = -1
    for i in range(i1 + 1, len(lst)):
        if lst[i] > lst[i1]:
            if i2 == -1 or lst[i2] > lst[i]:
                i2 = i

    swap(lst, i1, i2)
    reverse(lst, i1 + 1, len(lst) - 1)
    return int("".join(lst))


def reverse(lst, l, r):
    while l < r:
        swap(lst, l, r)
        l, r = l + 1, r - 1


def getAllPerms(num):
    perms = set()
    while num != -1:
        perms.add(num)
        num = nextPerm(num)
    return perms


def swap(lst, i1, i2):
    t = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = t


def check(perms, primes):
    for v1 in perms:
        if v1 not in primes:
            continue
        for v2 in perms:
            if v1 == v2 or v2 not in primes:
                continue
            (n2, n1) = (max(v1, v2), min(v1, v2))
            n3 = 2 * n2 - n1
            if n3 in perms and n3 in primes:
                return (n1, n2, n3)
    return None


def find():
    primes = sieve(10000)
    used = [False] * 10000
    perms = getAllPerms(1478)
    for i in range(1000, 10000):
        if used[i] == True:
            continue
        perms = getAllPerms(i)
        for num in perms:
            used[num] = True
        t = check(perms, primes)
        if t != None:
            print t


if __name__ == '__main__':
    find()
