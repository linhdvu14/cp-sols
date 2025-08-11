''' D. Shocking Arrangement
https://codeforces.com/contest/1798/problem/D
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
    if set(A) == {0}: return 'No', []

    A = deque(sorted(A))
    res = []
    s = 0
    while A:
        if s <= 0: a = A.pop()
        else: a = A.popleft()
        res.append(a)
        s += a

    return 'Yes', res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        a, b = solve(N, A)
        print(a)
        if b: print(*b)


if __name__ == '__main__':
    main()

