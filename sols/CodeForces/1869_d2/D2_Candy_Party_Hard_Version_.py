''' D2. Candy Party (Hard Version)
https://codeforces.com/contest/1869/problem/D2
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
BITS = 30

# 0100 = 1000 - 0100
# add: a -> +m|0, -(a-m)|+(a-m)
# sub: b -> -n|0, +(b-n)|-(b-n)
# -> now: +m -(a-m) -n +(b-n) = -a +b +2m -2n (1)
#    nxt: +(a-m) -(b-n) = +a -b -m +n         (2)
# any m, n s.t. (1) is 0 will result in same (2)

def solve(N, A):
    avg, r = divmod(sum(A), N)
    if r: return 'NO'

    def diff(x):
        for l in range(BITS):
            if (x >> l) & 1:
                r = l
                while r < BITS and (x >> r) & 1: r += 1
                for i in range(r, BITS):
                    if (x >> i) & 1: return -1, -1
                return l, r 
                
    bal = [0] * (BITS + 2)
    free_add = [0] * (BITS + 2)
    free_sub = [0] * (BITS + 2)
    for a in A:
        d = a - avg 
        if not d: continue
        if d > 0: add, sub = diff(d)
        else: sub, add = diff(-d)
        if sub == -1: return 'NO'

        if add - sub == 1: free_add[sub] += 1 
        elif sub - add == 1: free_sub[add] += 1
        else:   
            bal[add] += 1
            bal[sub] -= 1

    for i in range(BITS + 1):
        a, b = free_add[i], free_sub[i]
        d, rem = divmod(a - b - bal[i], 2)
        if rem: return 'NO'
        
        if d == 0: m = n = min(a, b)
        elif d > 0: m, n = d, 0 
        else: m, n = 0, -d
        if m > a or n > b: return 'NO'
    
        bal[i] += -a + b + 2 * m - 2 * n
        bal[i + 1] += a - b - m + n

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()


