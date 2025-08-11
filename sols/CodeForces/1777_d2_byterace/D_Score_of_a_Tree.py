''' D. Score of a Tree
https://codeforces.com/contest/1777/problem/D
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
MOD = 10**9 + 7

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


# u is 1 at time t iff u has an odd number of descendants at depth d that are set at time 0 -> 2^(N-1) ways
def solve(N, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    @bootstrap
    def dfs(u, p=-1):
        nonlocal res
        d = 1
        for v in adj[u]:
            if v == p: continue
            d = max(d, 1 + (yield dfs(v, u)))
        res = (res + m * d) % MOD 
        yield d

    m = pow(2, N - 1, MOD)
    res = 0
    dfs(0)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, edges)
        print(res)


if __name__ == '__main__':
    main()

