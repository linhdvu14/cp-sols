''' A. Likes
https://codeforces.com/contest/1802/problem/A
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
    pos = sum(1 for a in A if a > 0)
    neg = N - pos
    mx = list(range(1, pos + 1)) + list(range(pos - 1, pos - neg - 1, -1))
    mn = [1, 0] * neg + list(range(1, pos - neg + 1))
    return mx, mn


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        a, b = solve(N, A)
        print(*a)
        print(*b)


if __name__ == '__main__':
    main()

