
def compute():
    ind =1
    while ind!=1000000000:
        if buildFor(ind):
            print ind
            return
        ind+=1

def buildFor(num):
    nums=[num]
    for i in range(2,7):
        el = num*i
        if get_digs(el)!=get_digs(num):
            return False
        nums.append(el)
    return same(nums)


def same(nums):
    n1 = nums[0]
    for num in nums:
        if not sameDigs(n1,num):
            return False
    return True

def sameDigs(num1,num2):
    return get_digs(num1)==get_digs(num2)

def get_digs(num):
    lst=list()
    while num!=0:
        lst.append(num%10)
        num/=10
    return sorted(lst)



if __name__ == '__main__':
    compute()