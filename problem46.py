import math


def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


def sieve(MAX):
    primes = []
    sv = [True] * (MAX + 1)
    for i in range(2, MAX + 1):
        if sv[i] == False:
            continue
        primes.append(i)
        j = i * i
        while j <= MAX:
            sv[j] = False
            j += i
    return primes


def findClosest(primes, num):
    l, r = 0, len(primes)
    while l <= r:
        mid = l + (r - l) / 2
        if primes[mid] > num:
            r = mid - 1
        elif primes[mid] == num:
            return mid
        else:
            if mid == len(primes) - 1:
                return mid
            elif primes[mid + 1] > num:
                return mid
            l = mid + 1
    return -1


def canBeRepresented(num, primes):
    ind = findClosest(primes, num)
    if ind == -1:
        return False
    for i in range(0, ind + 1):
        val = num - primes[i]
        if val & 1 != 0:
            continue
        temp = val >> 1
        # print num,primes[i],val,temp
        if is_square(temp):
            return True
    return False


def solve(MAX):
    primes = sieve(MAX)
    for i in range(2, MAX + 1):
        if i & 1 == 0:
            continue
        if primes[findClosest(primes, i)] == i:
            continue
        ans = canBeRepresented(i, primes)
        if ans==False:
            print i
        # print i,ans


if __name__ == '__main__':
    solve(30033322)
