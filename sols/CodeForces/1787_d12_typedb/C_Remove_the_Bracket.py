''' C. Remove the Bracket
https://codeforces.com/contest/1787/problem/C
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

def solve(N, S, A):
    L, R = [0] * N, [0] * N 
    for i, a in enumerate(A):
        if a > S:
            L[i] = min(S, a - S)
            R[i] = max(S, a - S)
        else:
            R[i] = a
    
    l, r = A[0] * L[1], A[0] * R[1]
    for i in range(2, N - 1):
        l2 = min(l + R[i - 1] * L[i], r + L[i - 1] * L[i])
        r2 = min(l + R[i - 1] * R[i], r + L[i - 1] * R[i])
        l, r = l2, r2
    
    res = min(l + R[-2] * A[-1], r + L[-2] * A[-1])

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, S = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, S, A)
        print(res)


if __name__ == '__main__':
    main()
