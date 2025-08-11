''' B. XOR Palindromes
https://codeforces.com/contest/1867/problem/B
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

def solve(N, S):
    bad = 0
    for i in range(N // 2):
        if S[i] != S[N - 1 - i]: 
            bad += 1
    good = N // 2 - bad
    
    res = [0] * (N + 1)
    for x in range(bad, N + 1):
        r = x - bad
        if r % 2 == 0 and r // 2 <= good: res[x] = 1
        if r % 2 == 1 and N % 2 == 1 and (r - 1) // 2 <= good: res[x] = 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        res = solve(N, S)
        print(*res, sep='')


if __name__ == '__main__':
    main()

