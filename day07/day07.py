def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    lines = [list(line.strip('\n')) for line in lines] 

    return lines


def solve(lines):
    nlines = len(lines)
    nchars = len(lines[0])
    n_splits = 0
    for i in range(1,nlines):
        for j in range(nchars):
            if lines[i][j] == '.':
                if lines[i-1][j] in ('S', '|'):
                    lines[i][j] = '|'
            elif lines[i][j] == '^':
                if lines[i-1][j] == '|':
                    lines[i][j-1] = '|'
                    lines[i][j+1] = '|'
                    n_splits += 1

    return n_splits, lines

if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    lines = get_input(fname)

    ans, lines = solve(lines)

    print(f'The sum of all puzzle answers is {ans}')

