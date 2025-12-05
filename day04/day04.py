def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    return [line.strip() for line in lines]

def solve(lines):

    return None


if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    lines = get_input(fname)
