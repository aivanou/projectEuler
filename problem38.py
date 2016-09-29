import math

def isPandigital(s):
    if len(s)>9 or len(s)<9:
        return False
    lst = [0]*9
    for ch in s:
        val = ord(ch)-ord('1')
        if ch=='0':
            return False
        if lst[val]!=0:
            return False
        lst[val]=1
    return True

def mult(d,nums):
    return "".join([str(d*num) for num in nums])

def isPandigitalSeq(d,nums):
    return isPandigital(mult(d,nums))

def computeMax(nums):
    ind = 1
    maxVal = -1
    while True:
        val = mult(ind,nums)
        if len(val)>9:
            return maxVal
        if isPandigital(val):
            maxVal=max(maxVal,int(val))
        ind+=1
    return maxVal

def find():
    lst=[1,2]
    for i in range(3,10):
        mv = computeMax(lst)
        print mv
        lst.append(i)


if __name__ == '__main__':
    find()