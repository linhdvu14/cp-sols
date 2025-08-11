''' E. Caisa and Tree
https://codeforces.com/contest/463/problem/E
'''

import io, os, sys
input = sys.stdin.readline
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

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


def sieve(N):
    lpf = [0] * (N + 1)
    primes = []
    for i in range(2, N+1):
        if lpf[i] == 0:
            primes.append(i)
            lpf[i] = i
        for p in primes:
            if p * i > N or p > lpf[i]: break
            lpf[p * i] = p
    return lpf, primes


MAX = 2 * 10**6
from collections import deque

def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    # node depth
    depth = [-1] * N
    depth[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if depth[v] != -1: continue
            depth[v] = depth[u] + 1
            queue.append(v)
 
    # store last occurrences of each prime factor
    lpf, primes = sieve(MAX)
    last = {p: [] for p in primes}
    ans = [-2] * N
 
    @bootstrap
    def dfs(u, p=-1):
        ans[u] = -2

        # update ans
        a = A[u]
        while a > 1:
            f = lpf[a]
            if last[f] and (ans[u] == -2 or depth[last[f][-1]] > depth[ans[u]]): 
                ans[u] = last[f][-1]
            a //= f
 
        # update last
        a = A[u]
        while a > 1:
            f = lpf[a]
            if not last[f] or last[f][-1] != u: last[f].append(u)
            a //= f

        # recurse
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u,)
        
        # restore last
        a = A[u]
        while a > 1:
            f = lpf[a]
            if last[f] and last[f][-1] == u: last[f].pop()
            a //= f
        
        yield None 

    dfs(0)
    res = []
    for _ in range(Q):
        ts = list(map(int, input().split()))
        if len(ts) == 2 and ts[0] == 1:
            v = ts[1]
            res.append(ans[v-1] + 1)
        elif len(ts) == 3 and ts[0] == 2:
            v, a = ts[1], ts[2]
            A[v-1] = a 
            for p in primes: last[p] = []
            dfs(0)
 
    print(*res, sep='\n')


if __name__ == '__main__':
    main()


