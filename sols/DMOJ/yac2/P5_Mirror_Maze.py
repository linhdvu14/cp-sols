''' Yet Another Contest 2 P5 - Mirror Maze
https://dmoj.ca/problem/yac2p5
'''

import os, sys
input = sys.stdin.readline  # strip() if str

DEBUG = False #os.environ.get('debug') not in [None, '0']

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

MOD = 10**9 + 7

def mat_mul(a, b, N):
    res = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for i in range(N):
                res[r][c] = (res[r][c] + a[r][i] * b[i][c]) % MOD
    return res


def mat_pow(mat, e, N):
    res = [[0] * N for _ in range(N)]
    for i in range(N): res[i][i] = 1
    while e:
        if e & 1: res = mat_mul(res, mat, N)
        mat = mat_mul(mat, mat, N)
        e >>= 1
    return res


# solve individually for each bit b
# N + 1 states:
#   0..N-1: currently in room i, bit b off
#   N: currently in any room, bit b on (note a bit stays once it's been on)
# M[u][v] = transition prob from state u to state v

def main():
    N, L = list(map(int, input().split()))
    D = [list(map(int, input().split())) for _ in range(N)]
    p = pow(N-1, MOD-2, MOD)  # 1 / (N-1)
    
    res = [0 for _ in range(N)]
    def add_bit(b):
        # 1-step transition prob
        M = [[0 for _ in range(N+1)] for _ in range(N+1)]
        M[N][N] = 1
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if (D[i][j] >> b) & 1: M[i][N] = (M[i][N] + p) % MOD
                else: M[i][j] = p
        
        # L-step transition prob
        M = mat_pow(M, L, N+1)

        # prob of bit b on after L steps if start at room i
        for i in range(N): 
            res[i] = (res[i] + M[i][N] * (1 << b)) % MOD

    for b in range(30): add_bit(b)
    print(*res)


if __name__ == '__main__':
    main()