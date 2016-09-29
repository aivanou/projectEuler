
def find():
    l = 2000000
    sieve=[True]*(l+1)
    sm = 0
    for i in range(2,l):
        if sieve[i]==False:
            continue
        ind = i*i
        sm+=i
        while ind <l:
            sieve[ind]=False
            ind+=i
    print smAmicable

if __name__ == '__main__':
    find()