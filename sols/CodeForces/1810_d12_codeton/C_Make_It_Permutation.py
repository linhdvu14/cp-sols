''' C. Make It Permutation
https://codeforces.com/contest/1810/problem/C
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

def solve(N, C, D, A):
    A = sorted(list(set(A)))
    M = len(A)

    add = 0
    res = M * C + D 
    for i, a in enumerate(A):
        add += a - 1 if not i else a - A[i - 1] - 1
        res = min(res, add * D + (M - 1 - i) * C)

    return res + (N - M) * C


def main():
    T = int(input())
    for _ in range(T):
        N, C, D = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, C, D, A)
        print(res)


if __name__ == '__main__':
    main()

