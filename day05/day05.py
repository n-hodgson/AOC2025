def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    fresh_ranges = []
    available = []
    for line in lines:
        if '-' in line:
            low, high = line.split('-')
            fresh_ranges.append((int(low), int(high)))
        else:
            try:
                available.append(int(line))
            except ValueError:
                pass
    return fresh_ranges, available


def solve(grid):
    pass


if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    fresh_ranges, available = get_input(fname)

