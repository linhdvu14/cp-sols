''' D2. LuoTianyi and the Floating Islands (Hard Version)
https://codeforces.com/contest/1825/problem/D2
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
def precalc(N, mod):
    fact, inv_fact = [1] * (N + 1), [1] * (N + 1)
    for i in range(1, N + 1): fact[i] = i * fact[i - 1] % mod
    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in range(N - 1, 0, -1): inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact

MOD = 10**9 + 7
MAX = 2 * 10**5
FACT, INV_FACT = precalc(MAX, MOD)

def nCk(n, k): return 0 if k > n else FACT[n] * INV_FACT[n - k] * INV_FACT[k] % MOD

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


# https://codeforces.com/blog/entry/116328?#comment-1028681
# always exists at least one center C
# can extend C to new center C2, if the direction from C to C2 has exactly K/2 islands
# so centers are connected on a single path
# for each node, count num configurations in which it's C2 to some C in its outer tree
def main():
    N, K = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    if K % 2: return 1
    
    @bootstrap
    def dfs(u, p=-1):
        nonlocal num
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u)
            size[u] += size[v]
        num += nCk(size[u], K // 2) * nCk(N - size[u], K // 2) % MOD
        yield None

    num = 0
    denom = nCk(N, K)
    size = [1] * N
    dfs(0)

    return (1 + num * pow(denom, MOD - 2, MOD)) % MOD



if __name__ == '__main__':
    res = main()
    print(res)
