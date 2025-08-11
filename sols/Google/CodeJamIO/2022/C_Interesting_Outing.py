''' Interesting Outing 
https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33bc7
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


def solve(N, edges):
    S = 0
    adj = [[] for _ in range(N)]
    for u, v, c in edges:
        adj[u-1].append((v-1, c))
        adj[v-1].append((u-1, c))
        S += c
    
    # weighted tree diameter
    @bootstrap
    def dfs(u, p=-1):
        nonlocal mx
        cands = []
        for v, c in adj[u]:
            if v == p: continue
            child_mx = yield dfs(v, u)
            cands.append(child_mx + c)
        if not cands: yield 0
        cands.sort(reverse=True)
        mx = max(mx, cands[0])
        if len(cands) > 1: mx = max(mx, cands[0] + cands[1])
        yield cands[0]

    mx = 0
    dfs(0)

    return 2*S - mx


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        edges = [tuple(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, edges)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

