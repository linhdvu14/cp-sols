''' Crying Colours
https://www.codechef.com/JAN222A/problems/CRYCOLR
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug')

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

def solve(N, C):
    res = 0

    # direct swaps
    for i in range(3):
        C[i][i] = 0
        for j in range(i):
            mn = min(C[i][j], C[j][i])
            res += mn
            C[i][j] -= mn
            C[j][i] -= mn

    # cyclic swaps
    wrong = [[v for v in row if v > 0] for row in C]
    if all(not row for row in wrong): return res
    assert all(len(row) == 1 for row in wrong)
    assert len(set(row[0] for row in wrong)) == 1
    res += wrong[0][0]*2
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = [list(map(int, input().split())) for _ in range(3)]
        out = solve(N, C)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

