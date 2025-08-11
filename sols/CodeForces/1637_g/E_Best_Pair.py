''' E. Best Pair
https://codeforces.com/contest/1637/problem/E
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

def solve(N, M, A, bad):
    bad = set(bad)

    cnt = {}
    for a in A: cnt[a] = cnt.get(a, 0) + 1

    cnt_mp = {}
    for a, c in cnt.items():
        if c not in cnt_mp: cnt_mp[c] = []
        cnt_mp[c].append(a)

    for k, v in cnt_mp.items(): cnt_mp[k] = sorted(v, reverse=True)
    cnt = sorted(cnt_mp.keys())

    # cnt has at most sqrt(N) values
    # at most m bad checks occur
    # overall O(m+n)
    res = -INF
    for ix, cx in enumerate(cnt):
        # check (x, y) have same cnt
        n = len(cnt_mp[cx])
        for i in range(n):
            for j in range(i):
                x, y = cnt_mp[cx][i], cnt_mp[cx][j]
                if (x, y) not in bad and (y, x) not in bad:
                    res = max(res, (x + y) * 2 * cx)
                    break

        # check (x, y) have different cnt
        for iy in range(ix):
            cy = cnt[iy]
            for x in cnt_mp[cx]:
                for y in cnt_mp[cy]:
                    if (x, y) not in bad and (y, x) not in bad:
                        res = max(res, (x + y) * (cx + cy))
                        break

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        bad = [tuple(map(int, input().split())) for _ in range(M)]
        out = solve(N, M, A, bad)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

