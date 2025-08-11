''' B. Swap and Reverse
https://codeforces.com/contest/1864/problem/B
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

def solve(N, K, S):
    S = list(S)

    if K % 2 == 0:
        S.sort()
    else:
        P = sorted(S[i] for i in range(0, N, 2))
        Q = sorted(S[i] for i in range(1, N, 2))
        S = [a + b for a, b in zip(P, Q)]
        if N % 2: S += [P[-1]]

    return S


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        S = input().decode().strip()
        res = solve(N, K, S)
        print(*res, sep='')


if __name__ == '__main__':
    main()

