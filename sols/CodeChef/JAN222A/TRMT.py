''' Tree Master
https://www.codechef.com/JAN222A/problems/TRMT
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug')

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


class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])


class LCA:
    def __init__(self, root, graph):
        self.time = [-1] * len(graph)
        self.path = [-1] * len(graph)
        P = [-1] * len(graph)
        t = -1
        dfs = [root]
        while dfs:
            node = dfs.pop()
            self.path[t] = P[node]
            self.time[node] = t = t + 1
            for nei, _ in graph[node]:
                if self.time[nei] == -1:
                    P[nei] = node
                    dfs.append(nei)
        self.rmq = RangeQuery(self.time[node] for node in self.path)

    def __call__(self, a, b):
        if a == b:
            return a
        a = self.time[a]
        b = self.time[b]
        if a > b:
            a, b = b, a
        return self.path[self.rmq.query(a, b)]


def solve():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        adj[u-1].append((v-1, w))
        adj[v-1].append((u-1, w))

    # let SV[x] = sum vertex weights from x to root
    #     SE[x] = sum edge weights from x to root
    #     SP[x] = SUM_{k=x..root} SE[k] * A[k]
    SV, SE, SP = [0]*(N+1), [0]*(N+1), [0]*(N+1)

    @bootstrap
    def dfs1(u, w=0, p=-1):
        SV[u] = A[u] + SV[p]
        SE[u] = w + SE[p]
        SP[u] = SP[p] + A[u] * SE[u]
        for v, w in adj[u]:
            if v != p: yield dfs1(v, w, u)
        yield None
    dfs1(0)
    
    # for each query (u, v), want SUM_{k=u..v} [sum_edge(u, k) - sum_edge(v, k)] * A[k]
    lca = LCA(0, adj)
    
    def calc(u, v, a):
        '''
        given u, v and a=lca(u, v)
        calc SUM_{k=u..v} sum_edge(u, k) * A[k]
        '''
        res = 0

        # SUM_{k=a+1..v} sum_edge(u, k) * A[k]
        res += SP[v] - SP[a] - SE[a] * (SV[v] - SV[a])
        res += (SE[u] - SE[a]) * (SV[v] - SV[a] + A[a])

        # SUM_{k=u..a} sum_edge(u, k) * A[k]
        res -= SP[u] - SP[a] - SE[a] * (SV[u] - SV[a])
        res += (SE[u] - SE[a]) * (SV[u] - SV[a])

        return res

    for _ in range(Q):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        a = lca(u, v)
        res = calc(u, v, a) - calc(v, u, a)
        print(res)


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()

