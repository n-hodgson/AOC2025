def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    return [line.strip() for line in lines]

def check_location(grid, x, y, win):
    xmax = len(grid[0])
    ymax = len(grid)
    n_rolls = 0
    for w in win:
        xd = x + w[0]
        yd = y + w[1]
        if (xd >=0) and (xd < xmax) and (yd >= 0) and (yd < ymax):    
            if grid[yd][xd] == '@':
                n_rolls += 1
                if n_rolls == 4:
                    return False

    return True


def solve(grid):

    imax = len(grid[0])
    jmax = len(grid)
    nlocations = 0
    win = [(0, 1), (1, 1), (1, 0), (1, -1), 
           (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for i in range(imax):
        for j in range(jmax):
            if grid[j][i] == '@':
                if check_location(grid, i, j, win):
                    nlocations += 1

    return nlocations


if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    grid = get_input(fname)

    ans = solve(grid)

    print(f'The number of accessible locations is {ans}')