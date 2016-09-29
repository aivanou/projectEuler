
import math as m

def allPerms(nums):
    printNext(nums,[])

def printNext(nums,perm):
    if len(perm)==len(nums):
        print perm
        return
    for num in nums:
        if num in perm:
            continue
        perm.append(num)
        printNext(nums,perm)
        perm.pop()

def find(nums, pos):
    f = fact(len(nums)-1)
    snap=[]
    nums = sorted(nums)
    c = len(nums)
    for i in range(1,c):
        # print pos,f,int(m.ceil(float(pos)/f))-1
        snapPos = int(m.ceil(float(pos)/f))-1
        snap.append(nums.pop(snapPos))
        pos%=f
        f/=c-i
    snap.append(nums[0])
    print snap

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

if __name__ == '__main__':
    find([0,1,2,3,4,5,6,7,8,9],1000000)