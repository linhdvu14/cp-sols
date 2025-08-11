''' C. Maximum Set
https://codeforces.com/contest/1796/problem/C
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

FACT, INV_FACT = [1] * 22, [1] * 22
for i in range(1, 22): FACT[i] = i * FACT[i - 1] % MOD
INV_FACT[-1] = pow(FACT[-1], MOD - 2, MOD)
for i in range(20, 0, -1): INV_FACT[i] = INV_FACT[i + 1] * (i + 1) % MOD


def solve(L, R):
    if L * 2 > R: return 1, R - L + 1

    c2 = 0
    x = L << 1
    while x <= R: 
        c2 += 1
        x <<= 1

    mult = 1 << c2
    c3 = res = 0
    while c2 >= 0:
        n1 = FACT[c2 + c3] * INV_FACT[c2] * INV_FACT[c3] % MOD
        n2 = R // mult - L + 1
        if n2 <= 0: break
        res = (res + n1 * n2) % MOD
        c2 -= 1
        c3 += 1
        mult = mult // 2 * 3

    return c2 + c3 + 1, res % MOD


def main():
    T = int(input())
    for _ in range(T):
        L, R = list(map(int, input().split()))
        res = solve(L, R)
        print(*res)


if __name__ == '__main__':
    main()

