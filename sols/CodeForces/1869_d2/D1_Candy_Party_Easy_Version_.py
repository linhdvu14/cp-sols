''' D1. Candy Party (Easy Version)
https://codeforces.com/contest/1869/problem/D1
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
                
    cnt = [0] * (BITS + 1)
    for a in A:
        d = a - avg 
        if not d: continue
        if d > 0: l, r = diff(d)
        else: r, l = diff(-d)

        if l == -1: return 'NO'
        cnt[l] += 1
        cnt[r] -= 1

    if any(c for c in cnt): return 'NO'
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

