''' B. Bit Flipping
https://codeforces.com/contest/1659/problem/B
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


def solve(N, K, S):
    cnt = [0] * N
    res = [1] * N
    flip = 0

    for i, c in enumerate(S):
        c ^= flip
        if (c == 1 and K % 2 == 1) or (c == 0 and K % 2 == 0 and K > 0):
            cnt[i] += 1
            flip ^= 1
            K -= 1
        if (c == 0 and K == 0): res[i] = 0

    cnt[N-1] += K
    res[N-1] ^= K % 2
    
    print(*res, sep='')
    print(*cnt)



def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        S = list(map(int, list(input().decode().strip())))
        solve(N, K, S)


if __name__ == '__main__':
    main()

