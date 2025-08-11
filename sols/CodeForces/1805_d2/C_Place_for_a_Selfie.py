''' C. Place for a Selfie
https://codeforces.com/contest/1805/problem/C
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
from bisect import bisect_left

# ax^2 + (b - k)x + c = 0 has no roots
# (b - k)^2 < 4ac
def solve(N, M, K, ABC):
    K.sort()

    res = []
    for a, b, c in ABC:
        i = bisect_left(K, b)
        thres = 4 * a * c
        if i < len(K) and (b - K[i]) ** 2 < thres: res += ['YES', K[i]]
        elif i and (b - K[i - 1]) ** 2 < thres: res += ['YES', K[i - 1]]
        else: res += ['NO']

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        K = [int(input()) for _ in range(N)]
        ABC = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, K, ABC)
        print(*res, sep='\n', end='\n\n')


if __name__ == '__main__':
    main()

