''' A. Vika and Her Friends
https://codeforces.com/contest/1848/problem/A
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

def solve(R, C, K, X, Y, A):
    p = (X + Y) % 2
    for x, y in A:
        if (x + y) % 2 == p:
            return 'NO'
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        R, C, K = list(map(int, input().split()))
        X, Y = list(map(int, input().split()))
        A = [list(map(int, input().split())) for _ in range(K)]
        res = solve(R, C, K, X, Y, A)
        print(res)


if __name__ == '__main__':
    main()

