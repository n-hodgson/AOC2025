from operator import add, mul
from functools import reduce

def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    lines = [l.strip('\n') for l in lines]

    # get the index of the operators
    # the operator is always at the first column 
    tmp = lines[-1]
    ops_idx = [i for i in range(len(tmp)) if tmp[i] in ('*', '+')]
    ops = tmp.strip('\n').split()
                
    n_puzzles = len(ops)
    n_nums = len(lines) - 1 
    puzzles = []

    for i in range(n_puzzles):
        start = ops_idx[i]
        if i < (n_puzzles - 1):
            end = ops_idx[i+1] - 1
            nums = [lines[j][start:end] for j in range(n_nums)]
        else:
            nums = [lines[j][start:] for j in range(n_nums)]

        puzzles.append(
            (nums, ops[i], max([len(n) for n in nums]))
        )
    return puzzles


def solve(puzzles):

    ops = {'*': mul,
           '+': add}

    total = 0 
    
    for s, op, maxl in puzzles:
        nums = []
        for i in range(maxl - 1, -1, -1):
            nums.append(int(''.join([n[i] for n in s])))

        total += reduce(ops[op], nums)
    
    return total

if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    puzzles = get_input(fname)

    ans = solve(puzzles)

    print(f'The sum of all puzzle answers is {ans}')

