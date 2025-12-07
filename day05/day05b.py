def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    fresh_ranges = []
    available = []
    for line in lines:
        if '-' in line:
            low, high = line.split('-')
            fresh_ranges.append([int(low), int(high)])
        else:
            try:
                available.append(int(line))
            except ValueError:
                pass
    return fresh_ranges, available

def solve(ranges):
    
    sranges = sorted(ranges)
    
    valid_ranges = [sranges[0]]
    
    for curr_start, curr_end in sranges[1:]:

        last_start, last_end = valid_ranges[-1]
        
        if curr_start <= last_end + 1:
            valid_ranges[-1] = (last_start, max(last_end, curr_end))
        else:
            valid_ranges.append((curr_start, curr_end))
    
    total = sum([x[1] - x[0] for x in valid_ranges])

    return total, valid_ranges

if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    fresh_ranges, available = get_input(fname)

    ans = solve(fresh_ranges)

    print(f'The number of available fresh ingredients is {ans}')

