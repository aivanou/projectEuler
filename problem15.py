
def find(n):
    m=[[0]*(n+1)]*(n+1)
    m[1][1]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            m[i][j]=m[i-1][j]+m[i][j-1]
    print m[n][n]

if __name__ == '__main__':
    find(21)