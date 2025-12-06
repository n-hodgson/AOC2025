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


def solve_grid(grid):

    imax = len(grid[0])
    jmax = len(grid)
    locations = []
    win = [(0, 1), (1, 1), (1, 0), (1, -1), 
           (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for i in range(imax):
        for j in range(jmax):
            if grid[j][i] == '@':
                if check_location(grid, i, j, win):
                    locations.append((i,j))

    return len(locations), locations

def solve(grid):
    tot_locations = 0

    while True:
        nlocations, locations = solve_grid(grid)
        tot_locations += nlocations
        for loc in locations:
            grid[loc[1]][loc[0]] = '.'

        if nlocations == 0:
            break

    return tot_locations


if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    grid = get_input(fname)

    for i in range(len(grid)):
        grid[i] = [s for s in grid[i]]

    ans = solve(grid)

    print(f'The number of accessible locations is {ans}')