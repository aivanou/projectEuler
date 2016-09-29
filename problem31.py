
def find():
    sums=[1,2,5,10,20,50,100,200]
    target = 200
    dp=[[0 for i in range(0,len(sums)+1)] for i in range(0,target+1)]
    dp[0][0]=1
    for i in range(1,len(sums)+1):
        dp[0][i]=1
    for curSum in range(1,target+1):
        for i in range(1,len(sums)+1):
            dp[curSum][i] += dp[curSum][i-1]
            if(curSum>=sums[i-1]):
                dp[curSum][i]+=dp[curSum-sums[i-1]][i]
    print dp[target][len(sums)]

def test():
    n=3
    num = 0
    m = 10
    for i in range(0,n):
        num=num|1<<i
    while True:
        print bin(num)
        num = next(num,m)
        if num==-1:
            break

def next(n,m):
    bitNum = 0
    currPerm = n
    if n > 1<<(m-1):
        return -1
    while n!=0:
        bit = n&(-n)
        if (1<<m) == bit:
            return -1
        if (bit<<1) & n==0:
            return (currPerm-bit+(bit<<1))
        n-=bit

if __name__ == '__main__':
    # find()
    test()
    # print bin(bitToMove(345,10))