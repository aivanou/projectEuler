
def find(num):
    start = num*num
    sp=[[0 for i in range(0,num)] for j in range(0,num)]
    for k in range(0,num/2+1):
        for i in range(0,num-k*2-1):
            sp[k][num-1-i-k]=start
            start-=1
        for i in range(0,num-k*2-1):
            sp[i+k][k]=start
            start-=1
        for i in range(0,num-k*2-1):
            sp[num-1-k][i+k]=start
            start-=1
        for i in range(0,num-k*2-1):
            sp[num-1-i-k][num-1-k]=start
            start-=1

    sm=0
    for i in range(0,num):
        # for j in range(0,num):
        sm+=sp[i][i]
        sm+=sp[i][num-1-i]
    print sm+1
    # for i in range(0,num):
    #     print "\t".join([str(v) for v in sp[i]])


if __name__ == '__main__':
    find(1001)