''' Yet Another Contest 5 P3 - Potted Plants
https://dmoj.ca/problem/yac5p3
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

def solve(N):
    # delete min edges s.t. all nodes have even degree
    adj = [set(i for i in range(N) if i != j) for j in range(N)]
    if N % 2 == 0:
        for i in range(0, N, 2):
            adj[i].remove(i + 1)
            adj[i + 1].remove(i)
    
    # find eulerian cycle
    st, w = [0], []
    while st:
        v = st[-1]
        if adj[v]:
            i = adj[v].pop()
            adj[i].remove(v)
            st.append(i)
        else:
            w.append(v + 1)
            st.pop()
    
    # add back edge (0, 1)
    if N % 2 == 0: w.append(2)
    
    return w + w[::-1]


 
def main():
    N = int(input())
    res = solve(N)
    print(*res)


if __name__ == '__main__':
    main()

