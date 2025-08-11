''' G2. Teleporters (Hard Version)
https://codeforces.com/contest/1791/problem/G2
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

def solve(N, C, A):
    dist = [(min(i + 1 + a, N - i + a), i + 1 + a) for i, a in enumerate(A)]
    dist.sort()

    pref = [0]
    for d, _ in dist: pref.append(pref[-1] + d)

    res = 0
    for i, (d, l) in enumerate(dist):  # first move
        can, lo, hi = -1, 0, N 
        while lo <= hi:
            mi = (lo + hi) // 2
            use = pref[mi] - (d if mi > i else 0)
            if use + l <= C: 
                can = mi
                lo = mi + 1
            else:
                hi = mi - 1

        if can > -1: res = max(res, can + (can <= i))


    return res


def main():
    T = int(input())
    for _ in range(T):
        N, C = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, C, A)
        print(res)


if __name__ == '__main__':
    main()

