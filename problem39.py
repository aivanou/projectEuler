def findNums(p):
    sm = 0
    for n1 in range(1,p-2):
        n2,n3=1,p-n1-1
        # print n1,n2,n3,n1+n2+n3
        while n2<=n3:
            if n3*n3==(n2*n2+n1*n1):
                sm+=1
                # print n1,n2,n3
            n2,n3=n2+1,n3-1
    # print sm
    return sm


def find():
    sm = 0
    p=0
    for i in range(3,1001):
        csm = findNums(i)
        if csm>sm:
            p=i
            sm=csm
    print sm,p

if __name__ == '__main__':
    find()