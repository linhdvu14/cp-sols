''' E. Alternating String
https://codeforces.com/contest/2008/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']
DEBUG_CASE = int(os.environ.get('case', 0))

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

def solve(N, S):
    L = [[0] * 26 for _ in range(N + 2)]
    for i, c in enumerate(S):
        for d in range(26):
            L[i][d] = L[i - 2][d] + (d != ord(c) - ord('a'))
    
    R = [[0] * 26 for _ in range(N + 2)]
    for i in range(N - 1, -1, -1):
        for d in range(26):
            R[i][d] = R[i + 2][d] + (d != ord(S[i]) - ord('a'))

    if N % 2 == 0: return min(L[N - 1]) + min(L[N - 2])

    res = N
    for i in range(N):
        s1 = s2 = N
        for c in range(26):
            s1 = min(s1, L[i - 1][c] + R[i + 2][c])
            s2 = min(s2, L[i - 2][c] + R[i + 1][c])
        res = min(res, 1 + s1 + s2)

    return res



def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        S = input().decode().strip()
        if DEBUG and DEBUG_CASE and t != DEBUG_CASE: continue
        res = solve(N, S)
        print(res)


if __name__ == '__main__':
    main()

