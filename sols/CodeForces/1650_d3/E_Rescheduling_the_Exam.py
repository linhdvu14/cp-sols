''' E. Rescheduling the Exam
https://codeforces.com/contest/1650/problem/E
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

def solve(N, D, A):
    # dists[i] = rest time for A[i]
    dists = []
    for i, a in enumerate(A):
        if i == 0: dists.append(a - 1)
        else: dists.append(a - A[i-1] - 1)

    mni, mnd = -1, INF
    for i, d in enumerate(dists):
        if d < mnd: 
            mni, mnd = i, d

    res = mnd
    for i in [mni-1, mni]:
        if i < 0: continue
        pa, mn, mx = 0, INF, -INF
        for j, a in enumerate(A):
            if j == i: continue
            mn = min(mn, a - pa - 1)
            mx = max(mx, a - pa - 1)
            pa = a
        mn = min(mn, max((mx-1)//2, D-pa-1))
        res = max(res, mn)

    return res


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, D = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, D, A)
        print(out)


if __name__ == '__main__':
    main()

