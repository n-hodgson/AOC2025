def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    return [line.strip() for line in lines]

def find_max(s, start=0, seqlen=12):
    out = []
    n = len(s)
    start = 0 

    for i in range(seqlen):
        maxnum = float('inf')
        end = (n - seqlen + 1) + i
        for j in range(start, end):
            if s[j] > maxnum:
                maxnum = s[j]
                start = j + 1
        out.append(maxnum)
    return out

def solve(lines):
    maxnums = []
    for line in lines:
        c = [int(i) for i in line]
        a = find_max(c)
        n = int(''.join([str(i) for i in a]))
        maxnums.append(n)

    return sum(maxnums), maxnums


if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    lines = get_input(fname)

    ans, max_joltages = solve(lines)

    print(f'The sum of max joltages = {ans}')
