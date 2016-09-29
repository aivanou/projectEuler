import math

def get_fract(num,den):
    return (num+den,den)

def expand(num,den):
    num+=den*2
    return (den,num)

def ndigs(num):
    n=0
    while num!=0:
        n+=1
        num/=10
    return n

def compute():
    num,den=5,12
    count=0
    for i in range(2,1001):
        num,den=expand(num,den)
        n1,d1=get_fract(num,den)
        if ndigs(n1)>ndigs(d1):
            print n1,d1
            count+=1
    print count

if __name__ == '__main__':
    compute()


