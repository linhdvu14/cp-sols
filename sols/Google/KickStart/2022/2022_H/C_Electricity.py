''' Electricity
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47c8e
'''

import os, sys
input = sys.stdin.readline
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

def solve(N, A, edges):
    deg = [0] * N 
    adj = [[] for _ in range(N)]
    adj_rev = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1; v -= 1
        if A[u] < A[v]: 
            adj[v].append(u)
            adj_rev[u].append(v)
            deg[v] += 1
        elif A[v] < A[u]: 
            adj[u].append(v)
            adj_rev[v].append(u)
            deg[u] += 1
    
    topo = []
    st = [u for u in range(N) if deg[u] == 0]
    while st:
        u = st.pop()
        topo.append(u)
        for v in adj_rev[u]:
            deg[v] -= 1
            if deg[v] == 0: st.append(v)
    
    dp = [1] * N 
    for u in topo:
        for v in adj[u]:
            dp[u] += dp[v]
    
    return max(dp)


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, A, edges)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()

