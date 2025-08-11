''' C. Dora and Search
https://codeforces.com/contest/1793/problem/C
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
    pos = [0] * (N + 1)
    for i, a in enumerate(A): pos[a] = i + 1

    l = mn = 1 
    r = mx = N
    while l < r:
        mnp, mxp = pos[mn], pos[mx]
        if mnp == l:
            mn += 1
            l += 1
        elif mnp == r:
            mn += 1
            r -= 1
        elif mxp == l:
            mx -= 1
            l += 1
        elif mxp == r:
            mx -= 1
            r -= 1
        else:
            return [l, r]

    return [-1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(*res)


if __name__ == '__main__':
    main()

