''' E. There Should Be a Lot of Maximums
https://codeforces.com/contest/1805/problem/E
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


# if count(MAD) >= 3, all splits can get MAD
# if count(MAD) == 2, all splits except along the path connecting nodes with A[u] == MAD can get MAD
def solve(N, edges, A):
    adj = [[] for _ in range(N)]
    for i, (u, v) in enumerate(edges):
        u -= 1; v -= 1
        adj[u].append((i, v))
        adj[v].append((i, u))
    
    cnt = {}
    for a in A: cnt[a] = cnt.get(a, 0) + 1
    
    mad2 = mad3 = 0
    for a, c in cnt.items():
        if c > 2: mad3 = max(mad3, a)
        elif c == 2: mad2 = max(mad2, a)
    
    if mad3 >= mad2: return [mad3] * (N - 1)
    u1, u2 = [u for u in range(N) if A[u] == mad2]

    # returns: whether on path u1..u2, subtree seen mad2 cands, subtree mad2
    @bootstrap
    def dfs(u, end, idx=-1):
        on_path = u == end
        seen = set()
        mad = 0
        if A[u] > mad3 and cnt[A[u]] == 2: seen.add(A[u])
        for ei, v in adj[u]:
            if ei == idx: continue
            new_on_path, new_seen, new_mad = yield dfs(v, end, ei)
            on_path |= new_on_path
            mad = max(mad, new_mad)
            if len(seen) < len(new_seen): seen, new_seen = new_seen, seen 
            for k in new_seen:
                if k in seen: mad = max(mad, k)
                else: seen.add(k)
        if not on_path: res[idx] = mad2 
        elif idx != -1: res[idx] = max(res[idx], mad, mad3)
        yield on_path, seen, mad
    
    res = [-1] * (N - 1)
    dfs(u1, u2)
    dfs(u2, u1)
    return res


def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    A = list(map(int, input().split()))
    res = solve(N, edges, A)
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

