''' C. Meximum Array
https://codeforces.com/contest/1629/problem/C
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

def solve(N, A):
    cnt = [0] * (N + 1)
    for a in A: cnt[a] += 1

    mex = N + 1
    for a, c in enumerate(cnt):
        if c == 0:
            mex = a
            break

    res = []
    seen = set()
    nmex = mex
    for a in A:
        if a < mex: seen.add(a)
        cnt[a] -= 1
        if cnt[a] == 0: nmex = min(nmex, a)
        if len(seen) == mex:
            res.append(mex)
            seen = set()
            mex = nmex
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(len(out))
        print(*out)


if __name__ == '__main__':
    main()

