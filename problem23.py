
def find():
    limit=28123
    nums=[]
    for i in range(1,limit+1):
        if isAbundant(i):
            nums.append(i)
    sm = 0
    for i in range(1,limit+1):
        if not canBeMade(nums,i):
            sm += i
            #print i
    # print nums
    print sm


def canBeMade(nums, target):
    (l,r)=(0,len(nums)-1)
    while l<=r:
        if nums[l]+nums[r]>target:
            r-=1
        elif nums[l]+nums[r]<target:
            l+=1
        else:
            return True
    return False

def isAbundant(num):
    return sum(getDivs(num))>num

import math as m

def getDivs(num):
    divs=[1]
    for i in range(2,int(m.sqrt(num)+1)):
        if num%i==0:
            divs.append(i)
            if num/i!=i:
                divs.append(num/i)
    return divs

if __name__ == '__main__':
    find()