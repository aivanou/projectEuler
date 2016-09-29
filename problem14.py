
chain={}

def compute(n):
    ind = 0
    while n!=1:
        if n in chain:
            return ind+chain[n]
        if n%2==0:
            n/=2
        else:
            n=n*3+1
        ind+=1
    chain[n]=ind
    return ind

def find():
    mx = 0
    number = 0
    for i in range(10,1000000):
        cr = compute(i)
        if cr>mx:
            mx=cr
            number=i
    print number

if __name__ == '__main__':
    find()