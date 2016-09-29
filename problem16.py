import math

def find():
    v1 = int(math.pow(2,1000))
    sm = 0
    while v1!=0:
        sm+=v1%10
        v1/=10
    print sm

if __name__ == '__main__':
    find()