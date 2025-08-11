''' D1. LuoTianyi and the Floating Islands (Easy Version)
https://codeforces.com/contest/1825/problem/D1
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


def main():
    N, K = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    if K == 1 or K == 3: return 1

    @bootstrap
    def dfs(u, p=-1):
        nonlocal num
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u)
            size[u] += size[v]
            num -= size[v] * (size[v] - 1) // 2 % MOD 
        up = N - size[u]
        num -= up * (up - 1) // 2 % MOD
        yield None

    num = N * N * (N - 1) // 2 % MOD
    size = [1] * N
    dfs(0)

    return num * pow(N * (N - 1) // 2, MOD - 2, MOD) % MOD



if __name__ == '__main__':
    res = main()
    print(res)

