''' C. Make it Alternating
https://codeforces.com/contest/1879/problem/C
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
MAX = 2 * 10**5

FACT = [1] * (MAX + 1)
for i in range(1, MAX + 1): FACT[i] = FACT[i - 1] * i % MOD


def solve(S):
    cnt, ways, n = 0, 1, 1
    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            cnt += n - 1
            ways = ways * n % MOD
            n = 0 
        n += 1
    
    cnt += n - 1
    ways = ways * n % MOD * FACT[cnt] % MOD

    return cnt, ways


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        res = solve(S)
        print(*res)


if __name__ == '__main__':
    main()

