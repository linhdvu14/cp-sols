''' Magnet Sort
https://www.codechef.com/LTIME105A/problems/MAGNETSORT
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

def solve(N, A, S):
    B = sorted(A)
    if all(a == b for a, b in zip(A, B)): return 0
    if len(set(S)) == 1: return -1
    
    lo, hi = 0, N-1
    seen = set()
    while lo < N and A[lo] == B[lo]:
        seen.add(S[lo])
        lo += 1
    while hi >= 0 and A[hi] == B[hi]:
        seen.add(S[hi])
        hi -= 1
    if 0 <= lo < N: seen.add(S[lo])
    if 0 <= hi < N: seen.add(S[hi])
    return 1 if len(seen) == 2 else 2


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        S = input().decode().strip()
        out = solve(N, A, S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

