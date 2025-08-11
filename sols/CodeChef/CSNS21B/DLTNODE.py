''' Sardar and GCD
https://www.codechef.com/CSNS21B/problems/DLTNODE
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


def gcd(a, b):  # assume non-neg
    if a < b: a, b = b, a
    while b > 0: a, b = b, a % b
    return a


def solve(N, edges, vals):
    # make tree
    children = [set() for _ in range(N)]
    for u, v in edges:
        children[u-1].add(v-1)
        children[v-1].add(u-1)

    @bootstrap
    def dfs_clean(u, par=-1):
        if par != -1: 
            children[u].remove(par)
        for v in children[u]:
            yield dfs_clean(v, u)
        children[u] = list(children[u])
        yield None
    
    dfs_clean(0)

    # gcd_down[u] = gcd of subtree rooted at u
    # sub_sum[u] = sum gcd_down[v] for v in children[u]
    gcd_down = [-1]*N
    sub_sum = [0]*N
    
    @bootstrap
    def dfs_down(u):
        g = vals[u]
        s = 0
        for v in children[u]:
            yield dfs_down(v)
            g = gcd(g, gcd_down[v])
            s += gcd_down[v]
        gcd_down[u] = g
        sub_sum[u] = s
        yield None
        
    dfs_down(0)

    # gcd_up[v] = gcd of cc containing u=par[v] if disconnect (u, v)
    gcd_up = [-1]*N
    res = sub_sum[0]

    # gu = gcd of cc containing par[u] if disconnect (par[u], u)
    # update:
    # * gcd_up[v] for v in children[u]
    # * res if remove each v
    @bootstrap
    def dfs_up(u, gu=-1): 
        nonlocal res
        NC = len(children[u])

        if NC > 0:
            # left[v] = gcd(..v)
            left = [1]*NC
            left[0] = gcd_down[children[u][0]]
            for i in range(1, NC):
                left[i] = gcd(left[i-1], gcd_down[children[u][i]])

            # right[v] = gcd(v..)
            right = [1]*NC
            right[-1] = gcd_down[children[u][-1]]
            for i in range(NC-2, -1, -1):
                right[i] = gcd(right[i+1], gcd_down[children[u][i]])
            
            # disconnect (u, v)
            g = vals[u]
            if gu != -1: g = gcd(g, gu)
            for i, v in enumerate(children[u]):
                gv = g
                if i >= 1: gv = gcd(gv, left[i-1])
                if i <= NC-2: gv = gcd(gv, right[i+1])
                gcd_up[v] = gv
                res = max(res, sub_sum[v] + gv)
                yield dfs_up(v, gv)
        yield None

    dfs_up(0)

    return res



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        vals = list(map(int, input().split()))
        out = solve(N, edges, vals)
        print(out)


if __name__ == '__main__':
    main()

