def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    lines = [list(line.strip('\n')) for line in lines] 

    return lines


def solve(lines):
    return 0

if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    lines = get_input(fname)

    ans = solve(lines)

    print(f'The sum of all puzzle answers is {ans}')

