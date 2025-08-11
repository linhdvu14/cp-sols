''' B. Getting Zero
https://codeforces.com/contest/1661/problem/B 
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

from collections import deque

MOD = 32768

DIST = [INF] * MOD
DIST[0] = 0

queue = deque([0])
while queue:
    x = queue.popleft()
    neis = [(x - 1) % MOD]
    if x % 2 == 0:
        neis.append(x >> 1)
        neis.append((x >> 1) + (MOD >> 1))
    for y in neis:
        if DIST[y] < INF: continue
        DIST[y] = 1 + DIST[x]
        queue.append(y)


def solve(N, A):
    return [DIST[a] for a in A]


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(*out)


if __name__ == '__main__':
    main()

