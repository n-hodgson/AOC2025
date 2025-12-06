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


def solve(fresh_ranges, available):
    is_fresh = []
    for a in available:
        for r in fresh_ranges:
            if a in range(r[0], r[1]+1):
                is_fresh.append(a)
                break

    return len(is_fresh), is_fresh



if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    fresh_ranges, available = get_input(fname)

    ans, is_fresh = solve(fresh_ranges, available)

    print(f'The number of available fresh ingredients is {ans}')

