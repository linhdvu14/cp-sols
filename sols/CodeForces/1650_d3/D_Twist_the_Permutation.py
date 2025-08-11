''' D. Twist the Permutation
https://codeforces.com/contest/1650/problem/D
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

def solve(N, A):
    res = []
    for n in range(N, 0, -1):
        found = False
        for i in range(n):
            if A[i] == n:
                found = True
                res.append((i+1)%n)
                A = A[i+1:n] + A[:i+1] + A[n:]
                break
        if not found: return [-1]
    res.reverse()
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(*out)


if __name__ == '__main__':
    main()

