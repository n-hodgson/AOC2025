def get_input(fname):

    with open(fname, 'r') as fid:
        line = fid.readline()

    lines = line.split(',')
    ids = []
    for line in lines: 
        a, b = line.split('-')
        ids.append((int(a), int(b)))
    return ids 

def solve(lines):
    pass

if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    ids = get_input(fname)

