''' Problem D: Second Flight
https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/D
'''

import io, os, sys
input = sys.stdin.readline #io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

def solve(N, M, Q, edges, queries):
    edges = {(u-1, v-1): w for u, v, w in edges}
    adj = [{} for _ in range(N)]
    for (u, v), w in edges.items():
        adj[u][v] = w
        adj[v][u] = w
    
    # <= sqrt(2M) nodes with deg >= sqrt(2M)
    # all 2 hops from big node take O(M)
    # precompute for all big nodes
    def bfs(u):
        res = [0] * N
        for v1, w1 in adj[u].items():
            for v2, w2 in adj[v1].items():
                if v2 == u: continue
                res[v2] += min(w1, w2)
        return res

    big_thres = int((2 * M) ** 0.5)
    big_res = {u: bfs(u) for u in range(N) if len(adj[u]) > big_thres}

    # ans
    res = [0] * Q
    for i, (u, v) in enumerate(queries):
        u -= 1; v -= 1
        if len(adj[u]) < len(adj[v]): u, v = v, u

        # count 1 hop separately
        if (u, v) in edges: res[i] += edges[u, v] * 2
        elif (v, u) in edges: res[i] += edges[v, u] * 2

        # use 2-hop precompute if have big node
        # else intersect adj set directly
        if u in big_res: 
            res[i] += big_res[u][v]
        else:
            for t, w2 in adj[v].items():
                res[i] += min(w2, adj[u].get(t, 0))
            
    return res


def main():
    T = int(input())
    for t in range(T):
        N, M, Q = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(N, M, Q, edges, queries)
        print(f'Case #{t+1}:', *res)


if __name__ == '__main__':
    main()

