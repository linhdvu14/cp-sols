''' B. LuoTianyi and the Table
https://codeforces.com/contest/1825/problem/B
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

def solve(R, C, A):
    A.sort()
    res = max(
        A[-1] * R * C - A[-1] - A[1] * (min(R, C) - 1) - A[0] * (R * C - min(R, C)),
        A[-2] * (min(R, C) - 1) + A[-1] * (R * C - min(R, C)) + A[0] - A[0] * R * C,
    )
    return res


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(R, C, A)
        print(res)


if __name__ == '__main__':
    main()

