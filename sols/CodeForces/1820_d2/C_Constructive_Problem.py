''' C. Constructive Problem
https://codeforces.com/contest/1820/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
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

def solve(N, A):
    seen = set(A)
    mex = 0
    while mex in seen: mex += 1
    mex += 1

    if mex not in seen:
        seen = set()
        free = 0
        for a in A:
            if a > mex or a in seen: free += 1
            if a < mex: seen.add(a)
        return 'Yes' if free else 'No'
   
    seen = set()
    for a in A:
        if a == mex: break 
        if a < mex: seen.add(a)
    for a in A[::-1]:
        if a == mex: break 
        if a < mex: seen.add(a)
    return 'Yes' if len(seen) == mex - 1 else 'No'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

