import math
import sys

def sieve(n):
    s = []
    for i in range(1, n + 1):
        s.append(True)
    for i in range(2, int(math.sqrt(float(n)))):
        if s[i] == False:
            continue
        j = i * i
        while j < len(s):
            s[j] = False
            j += i
    return s

def makeMatr(rows, cols):
    return [[0 for v in range(0, cols)] for v in range(0, rows)]

def printm(m):
    for r in m:
        for v in r:
            sys.stdout.write(str(v))
            sys.stdout.write("\t")
        print ""

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True


def spiral(rows, cols):
    m = makeMatr(rows, cols)
    num = rows*cols
    (indi, indj) = (rows - 1, cols - 1)
    for j in range(0,min(rows,cols)/2):
        for i in range(j,indj+1-j):
            m[indi-j][indj-i]=num
            num-=1
        for i in range(j+1,indi+1-j):
            m[indi-i][j]=num
            num-=1
        for i in range(j+1,indj+1-j):
            m[j][i]=num
            num-=1
        for i in range(j+1,indi-j):
            m[i][indj-j]=num
            num-=1
    m[rows/2][cols/2]=1
    return m


def findPercentage():
    (p,cl,ru,rd,lu,ld)=(5,5,13,25,17,21)
    while cl<60001:
        nl=cl+2
        ru+=2*(cl-1)+2*(nl-2)
        rd+=4*(nl-1)
        lu+=2*(cl-1)+2*(nl-1)
        ld+=cl*2+2*(nl-1)
        if isPrime(ru):
            p+=1
        if isPrime(rd):
            p+=1
        if isPrime(lu):
            p+=1
        if isPrime(ld):
            p+=1
        if float(p)/(2*nl-1)<0.1:
            break;
    return float(p)/(2*nl-1)

if __name__ == '__main__':
    print findPercentage()
