''' B. Lamps
https://codeforces.com/contest/1839/problem/B
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
from collections import deque

def solve(N, A):
    A.sort(key=lambda t: (t[0], -t[1]), reverse=True)
    res = 0
    on = deque([])
    while A:
        a, b = A.pop()
        res += b 
        on.append(a)
        x = len(on)
        while on and on[0] <= x: on.popleft()
        while A and A[-1][0] <= x: A.pop()

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

