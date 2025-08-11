''' Max Shift After XOR
https://www.codechef.com/LTIME109A/problems/MAXCYCSHIFT
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

# consider wrap-around array B = A + A
# value of rotated array starting at A[i] is num unique eles in: B[i], B[i]^B[i+1], ..., B[i]^...^B[i+N-1]
# i.e. num unique eles in: B[0]^..^B[i], B[0]^..^B[i+1], ..., B[0]^..^B[i+N-1]

def solve(N, A):
    pref = []
    x = 0
    for a in A + A:
        x ^= a
        pref.append(x)
    
    res = 0
    cnt = {}
    for i, p in enumerate(pref):
        cnt[p] = cnt.get(p, 0) + 1
        if i >= N:
            cnt[pref[i-N]] -= 1
            if cnt[pref[i-N]] == 0: cnt.pop(pref[i-N])
            res = max(res, len(cnt))

    return res



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

