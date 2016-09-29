def find(ma,mb):
    st = set()
    for a in range(2,ma+1):
        for b in range(2,mb+1):
            (base,pw) = dec(a,b)
            if (base,pw) in st:
                continue
            st.add((base,pw))
    print len(st)
    # print st

import math as m

def dec(a,b):
    pows = 1
    t = a
    while m.pow(t,pows)==a:
        nt = int(m.sqrt(t))
        if nt*nt==t:
            pows*=2
            t=nt
        else:
            return (t,b*pows)
    return (t,pows*b)

if __name__ == '__main__':
    find(99,99)
    # print(dec(10000,2))