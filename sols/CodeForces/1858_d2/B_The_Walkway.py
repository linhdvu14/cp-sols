''' B. The Walkway
https://codeforces.com/contest/1858/problem/B
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

def solve(N, M, D, A):
    A = [1] + A + [N + 1]

    tot = 0
    for i in range(1, M + 2):
        tot += (A[i] - A[i - 1] - 1) // D + 1
    
    mx, cnt = -INF, 0
    for i in range(1, M + 1):
        save = (A[i] - A[i - 1] - 1) // D + (A[i + 1] - A[i] - 1) // D + 1 - (A[i + 1] - A[i - 1] - 1) // D
        if save > mx: mx, cnt = save, 0
        if save == mx: cnt += 1

    return tot - mx, cnt


def main():
    T = int(input())
    for _ in range(T):
        N, M, D = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, M, D, A)
        print(*res)


if __name__ == '__main__':
    main()

