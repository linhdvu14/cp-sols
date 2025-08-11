''' DMOPC '21 Contest 7 P3 - Whack-an-Ishigami
https://dmoj.ca/problem/dmopc21c7p3
'''

############ MLE ############

import sys
input = sys.stdin.readline

INF = float('inf')

def main():
    N, M = map(int, input().split())
    S = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    rev_adj = [[] for _ in range(N)]
    deg = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        rev_adj[b-1].append(a-1)
        deg[a-1] += 1

    # toposort on reverse adj (i.e. pop nodes leading to nothing)
    # final order contains all nodes not leading into or inside cycle
    topo = []
    st = [u for u in range(N) if deg[u] == 0]
    while st:
        u = st.pop()
        topo.append(u)
        for v in rev_adj[u]:
            deg[v] -= 1
            if deg[v] == 0: st.append(v)
        
    del rev_adj, st, deg
    
    # push down flips using topo order
    topo.reverse()
    flip = [0] * N
    res = 0
    for u in topo:
        if (S[u] + flip[u]) % 2 == 1:
            res += 1
            flip[u] += 1
        for v in adj[u]:
            flip[v] += flip[u]
    
    # now only all nodes not leading into or inside cycle handled
    # remaining nodes cannot be flipped
    # so check that orig state is 0
    for u in range(N):
        if (S[u] + flip[u]) % 2 == 1:
            return -1

    return res


if __name__ == '__main__':
    out = main()
    print(out)