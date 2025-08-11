''' D. Maximize the Root
https://codeforces.com/contest/1997/problem/D
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

def solve(N, A, P):
    P = [-1] + [p - 1 for p in P]
    
    deg = [0] * N
    for i, p in enumerate(P):
        if i: 
            deg[p] += 1

    min_child = [INF] * N
    st = []
    for i, d in enumerate(deg):
        if not d:
            min_child[i] = A[i]
            st.append(i)

    while st:
        i = st.pop()
        up, dn = A[i], min_child[i]
        if not i: return up + dn
        p = P[i]
        min_child[p] = min(min_child[p], (dn if up > dn else up + (dn - up) // 2))
        deg[p] -= 1
        if not deg[p]: st.append(p)



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        P = list(map(int, input().split()))
        res = solve(N, A, P)
        print(res)


if __name__ == '__main__':
    main()

