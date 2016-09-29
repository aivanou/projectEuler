import math

def is_pal(digs):
    l,r=0,len(digs)-1
    while l<r:
        if digs[l]!=digs[r]:
            return False
        l+=1
        r-=1
    return True

def to_arr(num):
    digs=[]
    while num!=0:
        digs.append(num%10)
        num/=10
    return digs

def reverse(num):
    digs=to_arr(num)
    new_num=0
    for i in range(0,len(digs)):
        new_num*=10
        new_num+=digs[i]
    return new_num

def iteration(num):
    new_num = reverse(num)+num
    return (new_num,is_pal(to_arr(new_num)))

def process(num):
    for i in range(1,51):
        (num, ans) = iteration(num)
        if ans:
            return False
    return True

def compute():
    count=0
    for i in range(12,10000):
        is_lychrel = process(i)
        if is_lychrel:
            count+=1
    print count


if __name__ == '__main__':
    compute()


