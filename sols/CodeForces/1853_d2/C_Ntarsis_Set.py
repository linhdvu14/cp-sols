''' C. Ntarsis' Set
https://codeforces.com/contest/1853/problem/C
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
# https://codeforces.com/blog/entry/116916?#comment-1050571
def solve_1(N, K, A):
    if A[0] != 1: return 1

    x, i = 1, 0
    for _ in range(K):
        while i < N and x + i >= A[i]: i += 1
        x += i

    return x


from bisect import bisect_right
def solve_2(N, K, A):
    # does any ele in 1..x remain after K days
    def ok(x):
        for _ in range(K):
            x -= bisect_right(A, x)
        return x > 0
    
    lo, hi, res = 1, 10**11, -1
    while lo <= hi:
        mi = (lo + hi) // 2
        if ok(mi):
            res = mi 
            hi = mi - 1
        else:
            lo = mi + 1
    
    return res


solve = solve_1
def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(res)

def test():
    def printf(dead, pad=2):
        res = []
        for i, d in enumerate(dead):
            if d == 2: s = '*'  # newly dead
            elif d == 1: s = '.'
            else: s = str(i + 1)
            res.append(' ' * (pad - len(s)) + s)
        print(*res)

    idx = {1, 2, 4, 5, 6}
    print(*sorted(list(idx)))
    A = list(range(50))
    dead = [0] * len(A)
    for _ in range(20):
        printf(dead)
        dead = [1 if d else 0 for d in dead]
        B = []
        for i, a in enumerate(A):
            if i + 1 in idx: dead[a] = 2
            else: B.append(a)
        A = B 
        if not A: break


if __name__ == '__main__':
    main()


