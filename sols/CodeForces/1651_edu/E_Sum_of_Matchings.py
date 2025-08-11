''' E. Sum of Matchings
https://codeforces.com/contest/1651/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

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


# https://codeforces.com/contest/1651/submission/149130164

def main():
    N = int(input())
    adj = [[] for _ in range(2*N)]
    for _ in range(2*N):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    seen = [0] * (2*N)
    @bootstrap
    def dfs(u, cycle):
        seen[u] = 1
        cycle.append(u)
        for v in adj[u]:
            if seen[v]: continue
            yield dfs(v, cycle)
        yield None
    
    res = 0
    for u in range(N):
        if seen[u]: continue
        cycle = []
        dfs(u, cycle)

        # count how many ranges contain the entire cycle
        # need left/right range to cover cycle span
        S = len(cycle)
        mnl, mxl, mnr, mxr = INF, -INF, INF, -INF
        for v in cycle:
            if v < N:
                mnl = min(mnl, v)
                mxl = max(mxl, v)
            else:
                mnr = min(mnr, v-N)
                mxr = max(mxr, v-N)
        res += S // 2 * (mnl + 1) * (N - mxl) * (mnr + 1) * (N - mxr)

        # for each edge in cycle, count how many times in appears in a matching as the n-th edge of a path
        for i in range(S):
            mnl, mxl, mnr, mxr = INF, -INF, INF, -INF
            for d in range(S):
                j = cycle[(i+d) % S]
                if j < N:
                    mnl = min(mnl, j)
                    mxl = max(mxl, j)
                else:
                    mnr = min(mnr, j-N)
                    mxr = max(mxr, j-N)

                # path i..j has even vertices
                # count last edge (j-1, j)
                if d % 2 == 1: 
                    # align s.t. (mn1, mx1) on i's side and (mn2, mx2) on k's side
                    k = cycle[(i+S-1) % S] 
                    mn1, mx1, mn2, mx2 = mnl, mxl, mnr, mxr
                    if i % 2 == 0: k -= N  # i left, k right
                    else: mn1, mx1, mn2, mx2 = mn2, mx2, mn1, mx1
                    
                    # (mn2, mx2) must exclude k
                    if k < mn2: res += (mn1 + 1) * (N - mx1) * (mn2 - k) * (N - mx2)
                    if k > mx2: res += (mn1 + 1) * (N - mx1) * (mn2 + 1) * (k - mx2)

    return res



if __name__ == '__main__':
    out = main()
    print(out)

