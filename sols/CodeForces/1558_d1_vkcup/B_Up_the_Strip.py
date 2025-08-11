''' B. Up the Strip
https://codeforces.com/contest/1558/problem/B
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

def solve(N, MOD):
    lpf = [0] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if not lpf[i]:
            lpf[i] = i 
            primes.append(i)
        for p in primes:
            if p * i > N or p > lpf[i]: break 
            lpf[p * i] = p 

    dp = [0] * (N + 1)
    dp[1] = sub = 1
    div = 0
    for x in range(2, N + 1):
        y = x
        facs = [1]
        while y > 1:
            p, cnt = lpf[y], 0
            while y % p == 0:
                y //= p 
                cnt += 1
            for i in range(len(facs)):
                for j in range(1, cnt + 1):
                    f = facs[i] * p ** j 
                    facs.append(f)
                    if f != x: div += dp[f] - dp[f - 1]

        div += dp[1]
        dp[x] = (sub + div) % MOD 
        sub = (sub + dp[x]) % MOD

    return dp[-1]


def main():
    N, MOD = list(map(int, input().split()))
    res = solve(N, MOD)
    print(res)


def gen():
    for x in range(2, 20):
        jumps = {}
        for z in range(2, x + 1):
            y = x // z 
            if y not in jumps: jumps[y] = []
            jumps[y].append(z)
        keys = sorted(jumps.keys())
        jumps = {k: jumps[k] for k in keys}
        print(f'x={x} jumps={jumps}')       


if __name__ == '__main__':
    main()
