''' C. LuoTianyi and the Show
https://codeforces.com/contest/1825/problem/C
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

def solve(N, M, A):
    L = A.count(-1)
    R = A.count(-2)
    A = sorted(list(set(a for a in A if a > 0)))
    N = len(A)

    res = min(max(L, R) + N, M)
    for i, a in enumerate(A):
        l = min(L + i, a - 1)
        r = min(R + N - 1 - i, M - a)
        res = max(res, l + r + 1)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, M, A)
        print(res)


if __name__ == '__main__':
    main()

