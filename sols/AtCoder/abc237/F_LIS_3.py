''' F - |LIS| = 3
https://atcoder.jp/contests/abc237/tasks/abc237_f
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

MOD = 998244353

def main():
    N, M = list(map(int, input().split()))

    # dp[i][a][b][c] = num seqs of length i s.t. 
    # - min ending ele of length 1 lis is a
    # - min ending ele of length 2 lis is b
    # - min ending ele of length 3 lis is c
    dp = [[[[0] * (M+2) for _ in range(M+2)] for _ in range(M+2)] for _ in range(N+1)]
    dp[0][M+1][M+1][M+1] = 1

    for i in range(1, N+1):
        for a in range(1, M+2):
            for b in range(1, M+2):
                for c in range(1, M+2):
                    for x in range(1, M+1):  # put x as i-th ele of seq
                        if x <= a: dp[i][x][b][c] += dp[i-1][a][b][c]
                        elif x <= b: dp[i][a][x][c] += dp[i-1][a][b][c]
                        elif x <= c: dp[i][a][b][x] += dp[i-1][a][b][c]
    
    res = 0
    for a in range(1, M+1):
        for b in range(1, M+1):
            for c in range(1, M+1):
                res = (res + dp[N][a][b][c]) % MOD
    
    print(res)


if __name__ == '__main__':
    main()

