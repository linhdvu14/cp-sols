''' D. Cross Coloring
https://codeforces.com/contest/1644/problem/D
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

MOD = 998244353 


def solve(R, C, K, Q, ops):
    # whether a row/col will be colored over
    row_used = set()
    col_used = set()
    # num color blocks
    cnt = 0
    for r, c in ops[::-1]:
        r -= 1
        c -= 1
        if not ((r in row_used and c in col_used) or len(row_used) == R or len(col_used) == C): cnt += 1
        row_used.add(r)
        col_used.add(c)
    
    return pow(K, cnt, MOD)


def main():
    T = int(input())
    for _ in range(T):
        R, C, K, Q = list(map(int, input().split()))
        ops = [list(map(int, input().split())) for _ in range(Q)]
        out = solve(R, C, K, Q, ops)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

