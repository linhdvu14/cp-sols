''' Pyramid Traversal
https://www.codechef.com/DEC21B/problems/PYRAMIDMOVES
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------

MOD = 10**9 + 7
MAX = 10**9

# LEFT[i] = leftmost value of row i
LEFT = [1]  
cur = i = 1
while cur < MAX:
    cur += i
    i += 1
    LEFT.append(cur)


# FACT[n] = n! % MOD
N = 2 * (LEFT[-1] - LEFT[-2])
FACT = [1] * (N+1)
for i in range(2, N+1):
    FACT[i] = (i * FACT[i-1]) % MOD


# INVFACT[n] = (1 / n!) % MOD
# a^(-1) = a^(p-2) mod p for p prime
INVFACT = [1] * (N+1)
for i in range(1, N+1):
    INVFACT[i] = pow(FACT[i], MOD-2, MOD)


def get_coords(val):
    # triangle row and col
    row, lo, hi = -1, 0, len(LEFT)-1
    while lo <= hi:
        mi = (lo+hi) // 2
        if LEFT[mi] <= val:
            row = mi
            lo = mi+1
        else:
            hi = mi-1
    col = val - LEFT[row]

    # slanted coords
    m = col
    n = LEFT[row+1] - LEFT[row] - m - 1

    return m, n



def solve(S, E):
    ms, ns = get_coords(S)
    me, ne = get_coords(E)
    m, n = me - ms, ne - ns
    if m < 0 or n < 0: return 0

    # C(m+n, m) = (m+n)! / m! / n!
    res = FACT[m+n] * INVFACT[m] * INVFACT[n]
    res %= MOD

    return res
    


def main():
    T = int(input())
    for _ in range(T):
        S, E = list(map(int, input().split()))
        out = solve(S, E)
        print(out)


if __name__ == '__main__':
    main()

