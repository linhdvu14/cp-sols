''' E. Middle Duplication
https://codeforces.com/contest/1623/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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


def main():
    N, K = list(map(int, input().split()))
    S = input().decode().strip()

    L, R = [-1]*N, [-1]*N
    for p in range(N):
        l, r = map(int, input().split())
        L[p], R[p] = l-1, r-1

    # inorder
    inorder = []

    @bootstrap
    def dfs1(u):
        if L[u] > -1: yield dfs1(L[u])
        inorder.append(u)
        if R[u] > -1: yield dfs1(R[u])
        yield None
    dfs1(0)

    # can duplicate if next different node exists and is greater
    good = [False]*N
    last = ''
    for i in range(N-2, -1, -1):
        u, v = inorder[i], inorder[i+1]
        if S[u] != S[v]: last = S[v]
        if S[u] < last: good[u] = True

    # greedily duplicate following inorder 
    # cost = cost if duplicate u; equals distance from u to nearest dup ancestor
    dup = [False]*N

    @bootstrap
    def dfs2(u, cost=1):
        nonlocal K
        if cost > K: yield

        # dup leftmost possible descendant
        if L[u] > -1:
            yield dfs2(L[u], cost+1)
            
        # left subtree dup; cost to dup u alr counted
        if L[u] > -1 and dup[L[u]]: 
            dup[u] = True

        # left subtree undup; subtract cost to dup u and its ancestors
        elif good[u]:
            dup[u] = True
            K -= cost
        
        # can only dup right subtree if u dup
        if R[u] > -1 and dup[u]: 
            yield dfs2(R[u], 1)
        
        yield None

    dfs2(0)

    # output
    print(''.join(S[u]*2 if dup[u] else S[u] for u in inorder))


if __name__ == '__main__':
    main()

