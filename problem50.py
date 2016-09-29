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


def bs(arr, num):
    (l, r) = (0, len(arr) - 1)
    while l <= r:
        mid = (l + r) / 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def find():
    limit = 1000001
    primes = sieve(limit + 1)
    psum = [0]
    for i in range(0, len(primes)):
        psum.append(psum[i] + primes[i])
    mn = 0
    num = 0
    # print primes, bs(primes, 13)
    # print psum
    for i in range(0, limit):
        for j in range(1, i + 1):
            (l, r) = (i - j, i)
            # print l, r, psum[r] - psum[l]
            if psum[r] - psum[l] > limit:
                break
            ind = bs(primes, psum[r] - psum[l])
            if mn < r - l and ind != -1:
                num = primes[ind]
                mn = r - l
                print mn, num
    print mn, num

if __name__ == '__main__':
    find()
