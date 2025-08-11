''' B. Square or Not
https://codeforces.com/contest/2008/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']
DEBUG_CASE = int(os.environ.get('case', 0))

def debug(*args):   
    if not DEBUG: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

def solve(N, S):
    x = int(N**0.5)
    if x * x != N: return 'NO'
    for r in range(x):
        for c in range(x):
            v = S[r * x + c]
            if (r in [0, x - 1] or c in [0, x - 1]) and v == '0': return 'NO'
            if r not in [0, x - 1] and c not in [0, x - 1] and v == '1': return 'NO'
    return 'YES'


def main():
    T = int(input())
    for ti in range(T):
        N = int(input())
        S = input().decode().strip()
        if DEBUG and DEBUG_CASE and ti != DEBUG_CASE: continue
        res = solve(N, S)
        print(res)


if __name__ == '__main__':
    main()

