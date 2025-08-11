''' D. Range and Partition
https://codeforces.com/contest/1631/problem/D
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

def solve_N(N, K, A):
    # x, y must be eles of A
    # for each x, find min y s.t. SUM_{x <= k <= y} >= (N + K) / 2
    cnt = [0] * (max(A) + 1)
    for a in A: cnt[a] += 1
    cnt = [(a, c) for a, c in enumerate(cnt) if c > 0]

    M = len(cnt)
    mnl, mnr = 0, M-1
    s = l = 0
    for r in range(M):
        s += cnt[r][1]
        while l < r and 2*(s - cnt[l][1]) >= N+K:
            s -= cnt[l][1]
            l += 1
        if 2*s >= N+K and cnt[r][0] - cnt[l][0] < cnt[mnr][0] - cnt[mnl][0]:
            mnl, mnr = l, r
    
    # partition
    min_x, min_y = cnt[mnl][0], cnt[mnr][0]
    parts = []
    l = r = cin = cout = 0
    while r < N:
        while r < N and (cin <= cout or len(parts) == K-1):
            if min_x <= A[r] <= min_y:
                cin += 1
            else:
                cout += 1
            r += 1
        parts.append((l+1, r))
        l = r
        cin = cout = 0
    
    return min_x, min_y, parts


def solve_NlogN(N, K, A):
    mn, mx = min(A), max(A)
    cnt = [0] * (mx + 1)
    for a in A: cnt[a] += 1

    pref = [0]
    for c in cnt: pref.append(pref[-1] + c)

    min_x, min_y = mn, mx
    for x in range(mn, mx+1):
        if cnt[x] == 0: continue
        y, lo, hi = INF, x, mx
        while lo <= hi:
            mi = (lo + hi) // 2
            if 2 * (pref[mi+1] - pref[x]) >= N + K:
                y = mi
                hi = mi - 1
            else:
                lo = mi + 1
        if y - x < min_y - min_x: min_x, min_y = x, y

    # should greedily cut as soon as cin == cout+1, unless for last partition
    # thus can partition iff cin >= cout + K <-> cin >= N - cin + K
    parts = []
    l = r = cin = cout = 0
    while r < N:
        while r < N and (cin <= cout or len(parts) == K-1):
            if min_x <= A[r] <= min_y:
                cin += 1
            else:
                cout += 1
            r += 1
        parts.append((l+1, r))
        l = r
        cin = cout = 0

    return min_x, min_y, parts


solve = solve_N

def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        x, y, parts = solve(N, K, A)
        print(x, y)
        for p in parts: print(*p)


if __name__ == '__main__':
    main()

