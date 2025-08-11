''' E - Packing Potatoes
https://atcoder.jp/contests/abc258/tasks/abc258_e
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

def main():
    N, Q, X = list(map(int, input().split()))
    W = list(map(int, input().split()))

    # S[i] = num potatoes in box, if first potato is W[i]
    # P[i] = first potato of next box, if first potato in this box is i
    k, r = divmod(X, sum(W))
    S = [k * N] * N
    P = list(range(N))
    if r:
        pref = [0]
        for i in range(2*N): pref.append(pref[-1] + W[i % N])
        for i in range(N):
            j, lo, hi = -1, i + 1, len(pref) - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                if pref[mi] - pref[i] >= r:
                    j = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            S[i] += j - i
            P[i] = (i + S[i]) % N

    # find cycle containing 0
    path = []
    seen = [0] * N
    u = 0
    while not seen[u]:
        path.append(u)
        seen[u] = 1
        u = P[u]

    for i, v in enumerate(path):
        if v == u:
            path, cycle = path[:i], path[i:]
            break

    res = [] * Q
    for _ in range(Q):
        k = int(input()) - 1
        if k < len(path): i = path[k]
        else: i = cycle[(k - len(path)) % len(cycle)]
        res.append(S[i])

    print(*res, sep='\n')


if __name__ == '__main__':
    main()



