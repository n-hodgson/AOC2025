import math

def get_input(fname):

    with open(fname, 'r') as fid:
        line = fid.readline()

    lines = line.split(',')
    ids = []
    for line in lines: 
        a, b = line.split('-')
        ids.append((int(a), int(b)))
    return ids 

def has_duplicates(s):
    s = str(s)
    i = len(s)

    # if sequence is of len 1 it is invalid
    if i == 1:
        return False
    
    # for sequences were all numbers are the same
    # such as 99, 11 or 11111111 then they are automatically 
    # invalid
    if len(set(s)) == 1:
        return True
    
    # sequences with len <= 3 can only be invalid if all characters
    # are the same e.g. 99, 111, so we only care about sequences with
    # len > 3
    elif i > 3:

        for win in [k for k in range(2,i) if i%k == 0]:
            seq = [s[j:(j+win)] for j in range(0, i, win)]
            if len(set(seq)) == 1:
                return True
        
        return False
    
    else:
        return False

def check_range(start, end):
    duplicates = []
    for i in range(start, end+1):
        if has_duplicates(i):
            duplicates.append(i)
    return duplicates
        

def solve(ids):
    invalid_ids = []
    for id in ids:
        d = check_range(id[0], id[1])
        if d != []:
            invalid_ids.extend(d)
            if len(invalid_ids) == 331:
                print(id)

    return sum(invalid_ids), invalid_ids

if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    ids = get_input(fname)
    ans, invalid_ids_nh = solve(ids)

    print(f'The sum of invalid IDs: {ans}')