''' E. Unpleasant Strings
https://codeforces.com/contest/2104/problem/E
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

def main():
    N, K = list(map(int, input().split()))
    S = input().decode().strip()

    last = [-1] * K
    dp_jump = [[-1] * (N + 1) for _ in range(K)]
    dp_depth = [INF] * N
    for i in range(N - 1, -1, -1):
        mn = INF
        for k in range(K):
            dp_jump[k][i] = last[k]
            if last[k] == -1: mn = 0
            else: mn = min(mn, dp_depth[last[k]])
        dp_depth[i] = mn + 1
        last[ord(S[i]) - ord('a')] = i
    for k in range(K):
        dp_jump[k][-1] = last[k]

    def solve(S):
        i = -1
        for c in S:
            i = dp_jump[ord(c) - ord('a')][i]
            if i == -1: return 0
        return dp_depth[i]
    
    Q = int(input())
    res = [0] * Q
    for qi in range(Q):
        q = input().decode().strip()
        res[qi] = solve(q)
    
    print(*res, sep='\n')



if __name__ == '__main__':
    main()

