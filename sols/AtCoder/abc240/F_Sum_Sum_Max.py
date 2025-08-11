''' F - Sum Sum Max
https://atcoder.jp/contests/abc240/tasks/abc240_f
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

# prefix sum:         B[i] = sum(C[0..i])
# sum of prefix sums: A[i] = B[0] + B[1] + ... + B[i] --> check when B[i] stops increasing

# C: -1  -1   2   2  2  -3  -3
# B: -1  -2   0   2  4   1  -2
# A: -1  -3  -3  -1  3   4   2

def solve(N, M, C): 
    res = C[0][0]
    a = b = 0

    # find consecutive block-end Bs that crosses 0 from above
    # find the last idx before crossing 0
    for x, y in C:
        if b > 0 and b + x * y < 0:
            i = b // abs(x)  # add the first i out of y x's
            cand_a = a + b * i + x * i * (i+1) // 2
            res = max(res, cand_a)
        a += b * y + x * y * (y+1) // 2
        b += x * y

    res = max(res, a)
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        C = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, M, C)
        print(out)


if __name__ == '__main__':
    main()
