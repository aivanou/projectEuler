
def find():
    sm = 0
    nums=[]
    for i in range(1,10001):
        if i in nums:
            continue
        (bl,n1,n2) = isAmmicable(i,nums)
        if bl:
            sm+=n1+n2
    print sm

import math as m

def isAmmicable(num,nums):
    divs = getDivs(num)
    temp = sum(divs)
    if sum(getDivs(temp))==num:
        nums.append(num)
        if temp<=10000:
            nums.append(temp)
            if temp==num:
                print num,0
                return (False,num,0)
            print num,temp
            return (True,num,temp)
        return (True,num,0)
    return (False,0,0)

def getDivs(num):
    divs=[1]
    for i in range(2,int(m.sqrt(num)+1)):
        if num%i==0:
            divs.append(i)
            divs.append(num/i)
    return divs

if __name__ == '__main__':
    find()