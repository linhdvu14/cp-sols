''' D. River Locks
https://codeforces.com/contest/1700/problem/D
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

# should always use leftmost pipes
# m pipes are enough to fill all locks in t secs iff
# * m * t >= pref[N]
# * for all pipe i=1..m, pref[i+1] <= i * t (else large pipe in front may not fill)

def main():
    N = int(input())
    V = list(map(int, input().split()))
    
    # min time needed to fill all locks with all pipes open
    # for each lock, need spillover + own >= capacity i.e. num_locks_till_now * t >= vol_till_now
    # i * thres - pref[i] + thres >= v <--> (i + 1) * thres >= pref[i+1]
    pref = thres = 0
    for i, v in enumerate(V):
        pref += v
        thres = max(thres, (pref + i) // (i + 1))
    
    Q = int(input())
    res = [0] * Q
    S = sum(V)
    for i in range(Q):
        t = int(input())
        res[i] = -1 if t < thres else (S + t - 1) // t

    print(*res, sep='\n')


if __name__ == '__main__':
    main()

