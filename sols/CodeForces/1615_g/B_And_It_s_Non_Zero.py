''' B. And It's Non-Zero
https://codeforces.com/contest/1615/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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
MAX = 2*10**5

# C[n][i] = count number having bit i = 0 for all 1..n 
C = [[0]*32 for _ in range(MAX+1)]

for num in range(1, MAX+1):
    for i in range(32):
        C[num][i] = C[num-1][i]
        if (num >> i) & 1 == 0:
            C[num][i] += 1

def solve(L, R):
    cnt = [0]*32
    for i in range(32):
        cnt[i] = C[R][i] - C[L-1][i]
    return min(cnt)


def main():
    T = int(input())
    for _ in range(T):
        L, R = list(map(int, input().split()))
        out = solve(L, R)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

