from itertools import combinations

def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    return [line.strip() for line in lines]

def find_max_naive(s):
    n = len(s)
    maxnum = float('-inf')
    for i in range(n - 1):
        for j in range(i+1, n):
            num = int(s[i] + s[j])
            if num > maxnum:
                maxnum = num
    return maxnum

def solve(lines):
    maxnums = []
    for line in lines:
        a = find_max_naive(line)
        maxnums.append(a)
    
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
