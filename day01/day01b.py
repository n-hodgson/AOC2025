def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    return lines 

def solve(lines):

    current_pos = 50
    zero_count = 0

    for l in lines:
        direction = l[0]
        magnitude = int(l[1:].strip())
        start_pos = current_pos

        if direction == 'R':
            y = current_pos + magnitude
            current_pos = y % 100  
            zero_count += (y // 100)          
        elif direction == 'L':
            y = current_pos - magnitude
            current_pos = y % 100
            zero_count += abs((y-1) // 100)
            # avoid double counting zero
            if start_pos == 0:
                 zero_count -= 1
        else:
            raise Exception('unknown direction')
        
    
    return zero_count

if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)        
  
    lines = get_input(fname)
    passwd = solve(lines)
    print(f'Analysing {fname} for total zero crossings')
    print(f'The password is: {passwd}')
