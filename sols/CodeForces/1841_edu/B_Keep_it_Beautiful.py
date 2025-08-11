''' B. Keep it Beautiful
https://codeforces.com/contest/1841/problem/B
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

def solve(Q, queries):
    A = []
    res = [0] * Q
    lo, hi = -INF, INF
    for i, q in enumerate(queries):
        if lo <= q <= hi:
            lo = q 
            res[i] = 1
            A.append(q)
        elif hi is INF and q <= A[0]:
            lo, hi = q, A[0]
            res[i] = 1
            A.append(q)

    return res


def main():
    T = int(input())
    for _ in range(T):
        Q = int(input())
        queries = list(map(int, input().split()))
        res = solve(Q, queries)
        print(*res, sep='')


if __name__ == '__main__':
    main()

