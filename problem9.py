
def find():
    ln = 1000
    for i in range(1,ln):
        l=i+1
        r=ln
        while l<=r:
            if i+r+l==ln and i*i+l*l==r*r:
                print i*l*r
            if i+l+r<ln:
                l+=1
            elif i+l+r>ln:
                r-=1
            else:
                r-=1
                l+=1

if __name__ == '__main__':
    find()