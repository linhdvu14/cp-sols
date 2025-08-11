''' C. Divine Tree
https://codeforces.com/contest/2120/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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

def solve(N, M):
    if not N <= M <= N * (N + 1) // 2: return -1, []

    M -= N
    root, edges = None, []
    for i in range(N, 1, -1):
        if i - 1 <= M:
            if not root: root = i
            else: edges += [[root, i]]
            M -= i - 1
        else:
            edges.append([1, i])
    
    if not root: root = 1
    else: edges.append([1, root])

    return root, edges


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        root, edges = solve(N, M)
        print(root)
        for e in edges: print(*e)


if __name__ == '__main__':
    main()


