def isDistinct(n):
    nums=set()
    while n!=0:
        d = n%10
        if d in nums:
            return False
        nums.add(d)
        n/=10
    return True

def split(n,nums):
    while n!=0:
        d = n%10
        if d in nums: 
            return False
        nums.add(d)
        n/=10
    return True

def isPandigital(n1,n2,n3):
    nums=set()
    if not split(n1,nums):
        return False
    if not split(n2,nums):
        return False
    if not split(n3,nums):
        return False
    return len(nums)==9 and 0 not in nums


def find():
    mx = 10000
    prods=set()
    for i in range(1,101):
        for j in range(1,mx):
            prod = i*j
            if isPandigital(i,j,prod) and prod not in prods:
                prods.add(prod)
                print i,j,prod,sum(prods)

if __name__ == '__main__':
    find()