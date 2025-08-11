''' D. Required Length
https://codeforces.com/contest/1681/problem/D
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

def solve(N, x):
    if len(str(x)) > N: return -1

    queue = deque([(0, x)])
    seen = set()
    while queue:
        d, x = queue.popleft()
        s = str(x)
        if len(s) == N: return d
        used = [1] * 2 + [0] * 8
        for c in s: 
            c = int(c)
            if used[c]: continue
            used[c] = 1
            y = x * c
            if y in seen: continue
            seen.add(y)
            queue.append((d + 1, y))

    return -1


def main():
    N, x = list(map(int, input().split()))
    out = solve(N, x)
    print(out)


if __name__ == '__main__':
    main()

