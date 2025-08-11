''' C. k-th equality
https://codeforces.com/contest/1836/problem/C
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

def solve(A, B, C, K):
    K -= 1
    mna, mxa = 10 ** (A - 1), 10 ** A - 1
    mnb, mxb = 10 ** (B - 1), 10 ** B - 1
    mnc, mxc = 10 ** (C - 1), 10 ** C - 1

    for a in range(mna, mxa + 1):
        lb = max(mnb, mnc - a)
        rb = min(mxb, mxc - a)
        n = max(rb - lb + 1, 0)
        if n <= K: K -= n; continue
        return f'{a} + {lb + K} = {a + lb + K}'

    return -1


def main():
    T = int(input())
    for _ in range(T):
        A, B, C, K = list(map(int, input().split()))
        res = solve(A, B, C, K)
        print(res)


if __name__ == '__main__':
    main()

