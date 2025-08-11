''' E - Just one
https://atcoder.jp/contests/abc226/tasks/abc226_e
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

MOD = 998244353

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


# each vertex has exactly 1 out-edge
# so num edges == num vertices
# each cc is cyclic, possibly with out-edge from some vertices on cycle

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    seen = [False] * N

    @bootstrap
    def dfs(u):
        seen[u] = True
        cnt_v, cnt_e = 1, len(adj[u])
        for v in adj[u]:
            if seen[v]: continue
            tv, te = yield dfs(v)
            cnt_v += tv
            cnt_e += te
        yield cnt_v, cnt_e
            
    res = 1
    for u in range(N):
        if seen[u]: continue
        cnt_v, cnt_e = dfs(u)
        if 2 * cnt_v != cnt_e: res = 0
        res = (res * 2) % MOD
    
    print(res)


if __name__ == '__main__':
    main()

