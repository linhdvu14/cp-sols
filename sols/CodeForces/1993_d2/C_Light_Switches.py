''' C. Light Switches
https://codeforces.com/contest/1993/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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

def solve(N, K, A):
    A.sort()
    mxa = A[-1]
    l1, r1 = mxa, mxa + K - 1

    for a in A[:-1]:
        l2 = a + 2 * K * ((mxa - a) // (2 * K))
        r2 = l2 + K - 1
        if r2 >= l1:
            r1 = min(r1, r2)
        else:
            l2 += 2 * K
            r2 += 2 * K
            if l2 <= r1:
                l1 = max(l1, l2)
            else:
                return -1

    if l1 <= r1: return l1
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(res)


if __name__ == '__main__':
    main()

