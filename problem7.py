
def find():
    l = 1000000
    sieve=[True]*(l+1)
    mInd = 0
    for i in range(2,l):
        if sieve[i]==False:
            continue
        ind = i*i
        mInd+=1
        if mInd==10001:
            print i
        while ind <l:
            sieve[ind]=False
            ind+=i
    # print mInd

if __name__ == '__main__':
    find()