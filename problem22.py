
def find():
    sm = 0
    names = sorted(read('pb22.txt'))
    for i in range(0,len(names)):
        sm+=(i+1)*(sum([ord(c)-ord('A')+1 for c in names[i]]))
    print sm

def read(fname):
    with open(fname,'r') as f:
        names = [name[1:-1] for name in f.readline().split(',')]
        return names

if __name__ == '__main__':
    find()