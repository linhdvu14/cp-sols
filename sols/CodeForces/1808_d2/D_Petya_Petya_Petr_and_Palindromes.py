''' D. Petya, Petya, Petr, and Palindromes
https://codeforces.com/contest/1808/problem/D
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

from bisect import bisect_left, bisect_right

# 1) j - i + 1 <= k --> j <= k + i - 1
# 2) left bound: i - (k - (j - i + 1)) // 2 >= 0 --> j >= k - i - 1
# 3) right bound: j + (k - (j - i + 1)) // 2 < N --> j <= 2N - k - i
# --> k - i - 1 <= j <= min(k + i - 1, 2N - k - i)

def solve(N, K, A):
    if K == 1: return 0

    pos = [{}, {}]
    for i, a in enumerate(A):
        p = i % 2
        if a not in pos[p]: pos[p][a] = []
        pos[p][a].append(i)
    
    res = (N - K + 1) * (K // 2)
    for mp in pos:
        for a, p in mp.items():
            for i in p:
                l = bisect_left(p, max(i + 1, K - i - 1))
                r = bisect_right(p, min(K + i - 1, 2 * N - K - i)) - 1
                if l <= r: res -= r - l + 1
    return res


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    res = solve(N, K, A)
    print(res)


if __name__ == '__main__':
    main()

