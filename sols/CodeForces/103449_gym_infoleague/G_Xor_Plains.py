''' G. Xor Plains
https://codeforces.com/gym/103449/problem/G
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

def next_pow(val):
    res = 1
    while res <= val:
        res <<= 1
    return res


# XOR(1...n) = ?
# n % 4 = 3 --> 0   --> [1..n]
# n % 4 = 0 --> n   --> [1..n-2] (-> xor=n-1) + [1<<?] + [1<<? + (n-1)]
# n % 4 = 1 --> 1   --> [1..n-3] (-> xor=n-2) + [n-1] + [?, ?]
# n % 4 = 2 --> n+1 --> [1..n-2] (-> xor=n-2) + [1<<?] + [1<<? + n-2]
def solve1(n):  # tle
    if n % 4 == 3: return list(range(1, n+1))

    if n % 4 == 0:
        p = next_pow(n-1)
        return list(range(1, n-1)) + [p, p+n-1]
    
    if n % 4 == 2:
        p = next_pow(n-2)
        return list(range(1, n-1)) + [p, p+n-2]
    
    # n=21: [1..18,20,24,31] not [1..18,20,32,39]
    xor = (n-1) ^ (n-2)
    cand = n
    while xor^cand <= n: cand += 1
    return list(range(1, n-2)) + sorted([n-1, cand, xor^cand])


def solve(n):  # official; tle
    # [1..n-3]
    xor = 0
    for i in range(1, n-2): 
        print(i, end=' ')
        xor ^= i

    n1 = n-2 if xor^(n-2) > 0 else n-1
    xor ^= n1
    print(n1, end=' ')

    n2 = n1 + 1
    while xor^n2 <= n1: n2 += 1
    print(f'{n2} {xor^n2}')


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    for n in A:
        solve(n)


if __name__ == '__main__':
    main()

