def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    return lines 

def solve(lines):

    current = 50
    zero_count = 0

    for l in lines:
        direction = l[0]
        magnitude = int(l[1:].strip())

        if direction == 'R':
            current = (current + magnitude) % 100
        elif direction == 'L':
            current = (current - magnitude) % 100
        else:
            raise Exception('unknown direction')

        if current == 0:
            zero_count += 1

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
    print(f'Analysing {fname}')
    print(f'The password is: {passwd}')
