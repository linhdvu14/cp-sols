''' E. Power Board
https://codeforces.com/contest/1646/problem/E
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

def solve(N, M):
    K = N.bit_length()

    # cnt[k] = for k=1..K, num uniq vals of i*j where i=1..k, j=1..M
    cnt = [0]
    val_used = [0] * (M * K + 1)
    for k in range(1, K+1):
        add = 0
        kk = k
        while kk <= M * k:
            if not val_used[kk]: add += 1
            val_used[kk] = 1
            kk += k
        cnt.append(cnt[-1] + add)
    
    # for each x s.t. x != b^e for some b, count k = num rows of form x^e
    res = 1
    row_used = [0] * (N+1)
    for x in range(2, N+1):
        if row_used[x]: continue
        xx = x
        k = 0
        while xx <= N:
            row_used[xx] = 1
            k += 1
            xx *= x
        res += cnt[k]

    return res


def main():
    N, M = list(map(int, input().split()))
    out = solve(N, M)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

