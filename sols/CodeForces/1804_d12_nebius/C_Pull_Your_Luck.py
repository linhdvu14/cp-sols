''' C. Pull Your Luck
https://codeforces.com/contest/1804/problem/C
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

def solve(N, X, P):
    for i in range(1, min(P, 2 * N) + 1):
        if (X + i * (i + 1) // 2) % N == 0:
            return 'Yes'
    return 'No'


def main():
    T = int(input())
    for _ in range(T):
        N, X, P = list(map(int, input().split()))
        res = solve(N, X, P)
        print(res)


if __name__ == '__main__':
    main()

