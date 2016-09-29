import math

primes=[2,3,5,7,11,13,17]

def getDivisors(num):
    divs=set()
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            divs.add(i)
            divs.add(num/i)
    return divs

def isSpecial(arr):
    for i in range(1,len(arr)-2):
        num = toNumber(arr[i:i+3])
        divs = getDivisors(num)
        # print num,divs
        if primes[i-1] not in divs:
            return False 
    return True

def toNumber(a):
    num = 0
    for n in a:
        num=num*10+n
    return num

def perms(arr):
    perms(arr,0)

def perms(arr, ind=0):
    if len(arr)==ind:
        if isSpecial(arr):
            print arr
            return toNumber(arr)
        return 0
    sm =0 
    for i in range(ind,len(arr)):
        swap(arr,i,ind)
        sm+=perms(arr,ind+1)
        swap(arr,i,ind)

    return sm
def swap(a,i,j):
    t=a[i]
    a[i]=a[j]
    a[j]=t

if __name__ == '__main__':
    # print(isSpecial([1,4,0,6,3,5,7,2,8,9]))
    print perms([0,1,2,3,4,5,6,7,8,9])
