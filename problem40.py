def findDig(num,pos):
    return str(num)[pos]


def findByPos(pos):
    nums, digCnt,base,nxt=(0,1,9,9)
    while True:
        if pos<nxt:
            break
        pos-=nxt
        nums+=base
        base*=10
        digCnt+=1
        nxt=base*digCnt
    pos-=1
    res = pos % digCnt
    n = pos/digCnt
    num = nums+n
    print num+1,res,int(findDig(num+1,res))
    return int(findDig(num+1,res))


def find():
    ans =  findByPos(1)*\
           findByPos(10)*\
           findByPos(100)*\
           findByPos(1000)*\
           findByPos(10000)*\
           findByPos(100000)*\
           findByPos(1000000)
    print ans

if __name__ == '__main__':
    find()