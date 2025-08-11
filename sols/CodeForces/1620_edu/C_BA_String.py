''' C. BA-String
https://codeforces.com/contest/1620/problem/C
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

# MSB -> LSB
def solve_1(N, K, X, S):
    # radix count
    bases = [1]
    c = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'a':
            if c > 0: bases.append(bases[-1]*(c*K+1))
            c = 0
        else:
            c += 1  
    if c > 0: bases.append(bases[-1]*(c*K+1)) 
    bases = bases[:-1][::-1]

    # build
    X -= 1  # X-1 smaller numbers
    res = ''
    j = 0
    for i, char in enumerate(S):
        if char == 'a':
            res += char
        elif i == 0 or S[i-1] == 'a':  # do for first *
            mult, X = divmod(X, bases[j])
            res += 'b'*mult
            j += 1

    return res


# similar to convert to base 2
# LSB -> MSB
# X = m1 * b1 + m2 * (b1*b2) + m3 * (b1*b2*b3) + ...
def solve_2(N, K, X, S):
    X -= 1  # X-1 smaller numbers

    res = ''
    c = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'a':
            if c > 0: 
                X, m = divmod(X, c*K+1)
                res += 'b' * m
            c = 0
            res += 'a'
        else:
            c += 1  
    if c > 0: 
        X, m = divmod(X, c*K+1)
        res += 'b' * m

    return res[::-1]


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N, K, X = list(map(int, input().split()))
        S = input().decode().strip()
        out = solve(N, K, X, S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

