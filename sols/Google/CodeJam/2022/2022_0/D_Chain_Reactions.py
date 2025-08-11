''' Chain Reactions
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
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


def solve(N, F, P):
    # root at 0 = abyss
    N += 1
    F = [0] + F
    adj = [[] for _ in range(N)]
    for i, p in enumerate(P):
        adj[i+1].append(p)
        adj[p].append(i+1)
    
    # prop min bottleneck upward
    @bootstrap
    def dfs(u, p=-1):
        nonlocal res
        cands = []
        for v in adj[u]:
            if v == p: continue
            c = yield dfs(v, u)
            cands.append(c)
        if not cands: yield F[u]
        cands.sort()
        res += sum(cands[1:])
        yield max(F[u], cands[0])
    
    res = 0
    v = dfs(0)
    res += v
    return res


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        F = list(map(int, input().split()))
        P = list(map(int, input().split()))
        out = solve(N, F, P)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

