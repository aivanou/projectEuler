import math

def generate(n):
    nset=set()
    nums=[]
    for i in range(1,n+1):
        num = i*(3*i-1)/2
        nset.add(num)
        nums.append(num)
    return (nset, nums)


def find():
    (nset, nums) = generate(10000)
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]-nums[i] in nset and nums[j]+nums[i] in nset:
                print nums[i],nums[j],nums[j]-nums[i]


if __name__ == '__main__':
    find()