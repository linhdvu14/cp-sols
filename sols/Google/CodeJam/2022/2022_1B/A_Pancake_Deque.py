''' Pancake Deque 
https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d 
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

def solve(N, D):
    res = mx = 0
    while D:
        if D[0] < D[-1]:
            if D[0] >= mx: res += 1
            mx = max(mx, D.popleft())
        else:
            if D[-1] >= mx: res += 1
            mx = max(mx, D.pop())

    return res


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        D = deque(map(int, input().split()))
        out = solve(N, D)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

