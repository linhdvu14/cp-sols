''' C. Tea Tasting
https://codeforces.com/contest/1795/problem/C
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

def solve(N, A, B):
    ps = [0] * (N + 1)
    for i, b in enumerate(B): ps[i + 1] = ps[i] + b

    mul = []
    res = [0] * (N + 1)
    for i, a in enumerate(A):
        j, lo, hi = i, i, N 
        while lo <= hi:
            mi = (lo + hi) // 2
            if ps[mi] - ps[i] <= a:
                j = mi 
                lo = mi + 1
            else:
                hi = mi - 1
        mul += [(i, 1), (j, -1)]
        res[j] += a - ps[j] + ps[i]
    
    m = 0
    mul.sort()
    for i, d in mul:
        m += d 
        if d == 1: res[i] += m * B[i]

    return res[:-1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, A, B)
        print(*res)


if __name__ == '__main__':
    main()

