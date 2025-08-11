''' Digit Multiplication By K
https://www.codechef.com/FEB221A/problems/DIGMULK
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

MOD = 10**9 + 7

def mat_mul(a, b):
    '''2D matrix multiplication'''
    nr_a, nc_a, nr_b, nc_b = len(a), len(a[0]), len(b), len(b[0])
    assert nc_a == nr_b
    res = [[0]*nc_b for _ in range(nr_a)]
    for r in range(nr_a):
        for c in range(nc_b):
            for i in range(nc_a):
                res[r][c] += a[r][i] * b[i][c]
                res[r][c] %= MOD
    return res


def mat_pow(mat, e):
    '''matrix power: mat^e'''
    N = len(mat)
    if e == 1:
        res = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                res[i][j] = mat[i][j] % MOD
        return res

    half = mat_pow(mat, e//2)
    res = mat_mul(half, half)
    if e % 2 != 0: res = mat_mul(res, mat)
    return res


def solve(N, K, M, S):
    if M == 0 or K == 0: return N

    cnt = [0]*10
    for c in S: cnt[int(c)] += 1

    # trans[i][j] = count of digit j after multiplying digit i with K
    trans = [[0]*10 for _ in range(10)]
    for i in range(10):
        sj = str(i * K)
        for c in sj: trans[i][int(c)] += 1

    trans = mat_pow(trans, M)
    res = 0
    for c, row in zip(cnt, trans):
        res += c * sum(row)
        res %= MOD
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K, M = list(map(int, input().split()))
        S = input().decode().strip()
        out = solve(N, K, M, S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

