from operator import add, mul
from functools import reduce

def get_input(fname):

    with open(fname, 'r') as fid:
        lines = fid.readlines()

    lines = [line.strip().split() for line in lines]

    n_numbers = len(lines) - 1
    n_puzzles = len(lines[0])
    puzzles = []
    for i in range(n_puzzles):
        puzzles.append(
            ([int(lines[j][i]) for j in range(n_numbers)], lines[-1][i])
        )
    return puzzles


def solve(puzzles):

    ops = {'*': mul,
           '+': add}

    total = 0 
    
    for nums, op in puzzles:
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

