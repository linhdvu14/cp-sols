''' D. Imbalanced Arrays
https://codeforces.com/contest/1853/problem/D
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
    idx = deque(sorted(list(range(N)), key=lambda i: A[i]))
    res = [0] * N 
    sub = 0
    while idx:
        x = len(idx)
        if A[idx[0]] == sub:
            i = idx.popleft()
            res[i] = -x
        elif A[idx[-1]] == x + sub:
            i = idx.pop()
            res[i] = x 
            sub += 1
        else:
            return 'NO', []

    return 'YES', res



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

