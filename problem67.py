
from collections import deque

def find(filename):
    data = [[int(num) for num in line.rstrip('\n').split(' ')] for line in open(filename)]
    q=[data[0][0]]
    msum = 0 
    ind = 1
    while ind!=len(data):
        nq=[]
        nq.append(data[ind][0]+q[0])
        for i in range(1,len(data[ind])-1):
            val = data[ind][i]+max(q[i-1],q[i])
            msum = max(msum,val)
            nq.append(val)
        nq.append(data[ind][len(data[ind])-1]+q[-1])
        q=nq
        ind+=1
    print msum

if __name__ == '__main__':
    find("pb67.txt")