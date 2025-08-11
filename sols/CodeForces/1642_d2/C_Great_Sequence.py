''' C. Great Sequence
https://codeforces.com/contest/1642/problem/C
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

def solve(N, X, A):
    cnt = {}
    for a in A: cnt[a] = cnt.get(a, 0) + 1
    keys = sorted(cnt.keys())

    res = 0
    for k in keys:
        if cnt[k] == 0: continue
        if cnt.get(k*X, 0) == 0: 
            res += cnt[k]
        else:
            d = min(cnt[k], cnt[k*X])
            res += cnt[k] - d
            cnt[k*X] -= d

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, X, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

