''' Yet Another Contest 6 P2 - No More Telemarketers
https://dmoj.ca/problem/yac6p2
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


def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    root = -1
    adj = [[] for _ in range(N)]
    for i, p in enumerate(T):
        if p != -1: adj[p - 1].append(i)
        else: root = i 
    
    if S[root] != -1: return -1, []

    res = []
    st = [root]
    while st:
        u = st.pop()
        for v in adj[u]:
            if S[v] != u + 1: res.append((v + 1, u + 1))
            st.append(v)
    
    return len(res), res 


if __name__ == '__main__':
    n, tups = main()
    print(n)
    for t in tups: print(*t)

