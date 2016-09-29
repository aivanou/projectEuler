ft={}
def compute(n):
    ind = 12
    while True:
        if digs(fib(ind))>=1000:
            print ind
            break
        ind+=1

def fib(n):
    if n in ft:
        return ft[n]
    if n==1:
        return 1
    if n==2:
        return 1
    num = fib(n-1)+fib(n-2)
    ft[n]=num
    return num

def digs(n):
    s=0
    while n>0:
        s+=1
        n/=10
    return s

if __name__ == '__main__':
    compute(1)