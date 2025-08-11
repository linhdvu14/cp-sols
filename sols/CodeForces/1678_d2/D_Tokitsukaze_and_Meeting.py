''' D. Tokitsukaze and Meeting
https://codeforces.com/contest/1678/problem/D 
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

# col[i] = col[i-1] + (S[j] == 0 for all j % C == i % C, j < i)
# row[i] = row[i-C] + (last 1 ixd > i - C)

def solve(R, C, S):
    res = [0] * R * C
    row = [0] * C
    seen = [0] * C
    col, last = 0, -1

    for i, v in enumerate(S):
        if v == '1': 
            if not seen[i%C]: col += 1
            seen[i%C] = 1
            last = i
        if last != -1 and last > i - C: row[i%C] += 1
        res[i] = col + row[i%C]

    return res


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        S = input().decode().strip()
        out = solve(R, C, S)
        print(*out)


if __name__ == '__main__':
    main()

