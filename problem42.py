import math

def read(fname):
    with open(fname,'r') as f:
        names = [name[1:-1] for name in f.readline().split(',')]
        return names

def computeTriangleNumbers(mx):
    nums=set()
    for i in range(1,mx+1):
        nums.add(i*(i+1)/2)
    return nums

def toNum(word):
    return sum([ord(ch)-ord('A')+1 for ch in word])

def find():
    fname='pb42.txt'
    nums = computeTriangleNumbers(100000)
    c=0
    for name in read(fname):
        if toNum(name) in nums:
            c+=1
    print c

if __name__ == '__main__':
    find()