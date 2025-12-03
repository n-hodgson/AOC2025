def get_input(fname):

    with open(fname, 'r') as fid:
        line = fid.readline()

    lines = line.split(',')
    ids = []
    for line in lines: 
        a, b = line.split('-')
        ids.append((int(a), int(b)))
    return ids 

def is_duplicate(s):
    s = str(s)
    if len(s) % 2 != 0:
        return False
    else:
        i = int(len(s) / 2)
        return s[:i] == s[i:]

def check_range(start, end):
    duplicates = []
    for i in range(start, end+1):
        if is_duplicate(i):
            duplicates.append(i)
    return duplicates
        

def solve(ids):
    invalid_ids = []
    for id in ids:
        d = check_range(id[0], id[1])
        if d != []:
            invalid_ids.extend(d)

    return sum(invalid_ids)

if __name__=='__main__':
    
    import sys

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Error, no file')
        sys.exit(1)
  
    ids = get_input(fname)
    ans = solve(ids)

    print(f'The some of invalid IDs: {ans}')