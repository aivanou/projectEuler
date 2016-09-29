import math as m

def find():
    i=2
    sm=0
    while True:
        if sum([m.pow(v,5) for v in digs(i)])==i:
            print i
            sm+=i
            print 'sum:',sm
        # print i
        i+=1

def digs(n):
    l=[]
    while n!=0:
        # print n 
        l.append(n%10)
        n=n/10
    return l

if __name__ == '__main__':
    find()