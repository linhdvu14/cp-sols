''' Controlled Inflation 
https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb
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

def solve(N, groups):
    for i in range(N): groups[i].sort()
    
    # dp[i][0/1] = min cost to serve groups[0:i] s.t. groups[i-1] is in asc/desc order
    dp = [[INF] * 2 for _ in range(N)]

    for i in range(N):
        if not groups[i]: debug(i)
        d = groups[i][-1] - groups[i][0]
        if i == 0:
            dp[i][0] = groups[i][0] + d
            dp[i][1] = groups[i][-1] + d
        else:
            dp[i][0] = min(
                abs(groups[i][0] - groups[i-1][0]) + dp[i-1][1], 
                abs(groups[i][0] - groups[i-1][-1]) + dp[i-1][0],
            ) + d
            dp[i][1] = min(
                abs(groups[i][-1] - groups[i-1][0]) + dp[i-1][1],
                abs(groups[i][-1] - groups[i-1][-1]) + dp[i-1][0],
            ) + d

    return min(dp[-1])


def main():
    T = int(input())
    for t in range(T):
        N, _ = list(map(int, input().split()))
        groups = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, groups)
        print(f'Case #{t+1}: {out}')


def gen():
    import random
    random.seed(123)

    T = 2
    print(T)
    for _ in range(T):
        N = random.randint(2, 1000)
        P = random.randint(2, 100)
        print(N, P)
        for _ in range(N):
            gr = [random.randint(1, 1e9) for _ in range(P)]
            print(*gr)



if __name__ == '__main__':
    main()
    # gen()

