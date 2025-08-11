''' D. Triangle Coloring
https://codeforces.com/contest/1795/problem/D
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
    N = int(input())
    A = list(map(int, input().split()))

    G = N // 3
    fact, inv_fact = [1] * (G + 1), [1] * (G + 1)
    for i in range(1, G + 1): fact[i] = i * fact[i - 1] % MOD
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(G - 1, 0, -1): inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    res = fact[G] * inv_fact[G // 2] * inv_fact[G // 2] % MOD
    for i in range(G):
        a, b, c = A[3 * i], A[3 * i + 1], A[3 * i + 2]
        scores = [a + b, b + c, c + a]
        ways = scores.count(max(scores))
        res = res * ways % MOD

    print(res)


if __name__ == '__main__':
    main()

