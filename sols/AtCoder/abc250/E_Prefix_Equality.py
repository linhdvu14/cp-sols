''' E - Prefix Equality
https://atcoder.jp/contests/abc250/tasks/abc250_e
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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc

INF = float('inf')

# -----------------------------------------

def solve_1(N, A, B, Q, queries):
    import random
    random.seed(123)

    memo = {}
    def hash(x):
        if x not in memo: memo[x] = random.randrange(1 << 64)
        return memo[x]

    Ha = []
    x, seen = 0, set()
    for a in A: 
        if a not in seen:
            seen.add(a)
            x ^= hash(a)
        Ha.append(x)

    Hb = []
    x, seen = 0, set()
    for b in B: 
        if b not in seen:
            seen.add(b)
            x ^= hash(b)
        Hb.append(x)
    
    res = []
    for x, y in queries:
        if Ha[x-1] == Hb[y-1]: res.append('Yes')
        else: res.append('No')
    
    return res


def solve_2(N, A, B, Q, queries):
    fa = {A[i]: i for i in range(N-1, -1, -1)}
    fb = {B[i]: i for i in range(N-1, -1, -1)}

    # pa[i] = min j s.t. A[0..i] all appear in B[0..j]
    pa = [-1] * N 
    mx = -1
    for i, a in enumerate(A):
        if a not in fb: break
        pa[i] = mx = max(mx, fb[a])
    
    pb = [-1] * N
    mx = -1
    for i, b in enumerate(B):
        if b not in fa: break
        pb[i] = mx = max(mx, fa[b])

    res = ['No'] * Q
    for i, (x, y) in enumerate(queries):
        x -= 1; y -= 1
        if pa[x] == -1 or pb[y] == -1: continue
        if pa[x] <= y and pb[y] <= x: res[i] = 'Yes'
    
    return res


solve = solve_2


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    out = solve(N, A, B, Q, queries)
    print(*out, sep='\n')


if __name__ == '__main__':
    main()
