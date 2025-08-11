''' D. X(or)-mas Tree
https://codeforces.com/contest/1615/problem/D
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

from collections import deque

def solve():
    N, M = list(map(int, input().split()))

    # treat known santa as elves
    edges = []                    # tree edges
    obs = [[] for _ in range(N)]  # observed path xor

    for _ in range(N-1):
        u, v, w = list(map(int, input().split()))
        u -= 1
        v -= 1
        edges.append((u, v, w))
        if w != -1:
            w = bin(w).count('1') % 2
            obs[u].append((v, w))
            obs[v].append((u, w))
    
    for _ in range(M):
        u, v, w = list(map(int, input().split()))
        u -= 1
        v -= 1
        obs[u].append((v, w))
        obs[v].append((u, w))

    # check for conflict
    # note count(x^y) % 2 = (count(x) % 2) ^ (count(y) % 2)
    # color[u] = path xor bit parity of root..u
    color = [-1]*N
    for u in range(N):
        if color[u] != -1: continue
        color[u] = 0
        stack = deque([u])
        while stack:
            u = stack.pop()
            for v, w in obs[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ w
                    stack.append(v)
                elif color[v] != color[u] ^ w:
                    print('NO')
                    return
    
    # no conflict, fill in color
    # path_parity(u, v) = path_parity(u, root) ^ path_parity(v, root)
    print('YES')
    for u, v, w in edges:
        if w != -1:
            print(u+1, v+1, w)
        else:
            print(u+1, v+1, color[u]^color[v])



def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()

