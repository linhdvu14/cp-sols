''' C. Shinju and the Lost Permutation
https://codeforces.com/contest/1658/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

def solve(N, C):
    cnt = [0] * N  # start idx -> peak count
    for i, c in enumerate(C):
        cnt[(N-i) % N] = c

    if cnt.count(1) != 1: return False
    i = cnt.index(1)
    for _ in range(N-1):
        a, b = cnt[(i-1)%N], cnt[i]
        if not (a <= b or a == b + 1): return False
        i = (i-1) % N

    return True


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        out = solve(N, C)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

