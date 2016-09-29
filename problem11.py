def getR(m,i,j):
    if i+4>=len(m):
        return -1
    return m[i][j]*m[i+1][j]*m[i+2][j]*m[i+3][j]

def getL(m,i,j):
    if i-4<0:
        return -1
    return m[i][j]*m[i-1][j]*m[i-2][j]*m[i-3][j]

def getUp(m,i,j):
    if j-4<0:
        return -1
    return m[i][j]*m[i][j-1]*m[i][j-2]*m[i][j-3]

def getDown(m,i,j):
    if j+4>=len(m):
        return -1
    return m[i][j]*m[i][j+1]*m[i][j+2]*m[i][j+3]

def getLUDiag(m,i,j):
    if j-4<0 or i-4<0:
        return -1
    return m[i][j]*m[i-1][j-1]*m[i-2][j-2]*m[i-3][j-3]

def getRUDiag(m,i,j):
    if j+4>=len(m) or i-4<0:
        return -1
    return m[i][j]*m[i-1][j+1]*m[i-2][j+2]*m[i-3][j+3]

def getRDDiag(m,i,j):
    if j+4>=len(m) or i+4>=len(m):
        return -1
    return m[i][j]*m[i+1][j+1]*m[i+2][j+2]*m[i+3][j+3]

def getLDDiag(m,i,j):
    if j-4<0 or i+4>=len(m):
        return -1
    return m[i][j]*m[i+1][j-1]*m[i+2][j-2]*m[i+3][j-3]



def find():
    lines = [line.rstrip('\n') for line in open('pb11.txt')]
    m=[]
    for line in lines:
        m.append([int(v) for v in line.split(" ")])
    ans = 0
    for i in range(0,len(m)):
        for j in range(0,len(m)):
            ans = max(ans, getR(m,i,j))
            ans = max(ans, getL(m,i,j))
            ans = max(ans, getUp(m,i,j))
            ans = max(ans, getDown(m,i,j))
            ans = max(ans, getLUDiag(m,i,j))
            ans = max(ans, getRUDiag(m,i,j))
            ans = max(ans, getRDDiag(m,i,j))
            ans = max(ans, getLDDiag(m,i,j))
    print ans


if __name__ == '__main__':
    find()