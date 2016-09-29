import math

def getNDivs(n):
    cn = 0
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            cn+=2
    return cn+2


def find():
    nd = 500
    number = 1
    ind = 2
    while True:
        number +=ind
        ind+=1
        ndivs = getNDivs(number)
        if ndivs>=nd:
            print number
            return


if __name__ == '__main__':
    find()