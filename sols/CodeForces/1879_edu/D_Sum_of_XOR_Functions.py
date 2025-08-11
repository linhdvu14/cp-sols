''' D. Sum of XOR Functions
https://codeforces.com/contest/1879/problem/D
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
BITS = 30

def solve(N, A):
    res = 0

    for i in range(BITS):
        c0 = c1 = s0 = s1 = 0  # cnt/sum lengths of subarrays with even/odd 1s ending at each i
        for a in A: 
            b = (a >> i) & 1
            if not b:
                nc0 = c0 + 1
                nc1 = c1
                ns0 = s0 + c0 + 1 
                ns1 = s1 + c1
            else:
                nc0 = c1
                nc1 = c0 + 1
                ns0 = s1 + c1 
                ns1 = s0 + c0 + 1
            c0, c1, s0, s1 = nc0, nc1, ns0, ns1
            res = (res + (s1 << i)) % MOD

    return res 


def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    print(res)


if __name__ == '__main__':
    main()

'''
0 1 0 0 1 0 0 1 0

sum_l * cnt_r + sum_r * cnt_l

'''