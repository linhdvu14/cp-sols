''' E. Madoka and the Sixth-graders
https://codeforces.com/contest/1647/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

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

from heapq import heappush, heappop

def solve(N, P, A):
    P = [p-1 for p in P]
    A = [a-1 for a in A]

    # find num total rounds
    K = 0 if max(A) == N-1 else (max(A) - N + 1) // len(set(range(N)) - set(P))

    # pretend the students do not get removed but only move desk to desk
    # but only the smallest among all students currently at a given desk is considered sitting
    # let V[A[i]] = all desks j=0..N-1 s.t. the student originally at desk j is at desk i after K rounds 
    L = (K+1).bit_length()
    up = [[0]*L for _ in range(N)]
    for u, v in enumerate(P): up[u][0] = v
    for l in range(1, L):
        for i in range(N):
            up[i][l] = up[up[i][l-1]][l-1]

    V = [[] for _ in range(N)]
    for j in range(N):
        i, lv = j, K
        for l in range(L-1, -1, -1):
            if lv >= (1 << l):
                i = up[i][l]
                lv -= 1 << l
        if 0 <= A[i] < N: heappush(V[A[i]], j)
    
    # iterate over a=0..N-1
    # if V[a] non-empty, then student a must originally be at one of desks V[a]
    # if V[a] empty, then student a must end up sitting in same desk as some student b < a after K rounds
    # so student a must originally be at some V[b] where b < a
    res = [-1] * N
    cands = []
    for a in range(N):
        if V[a]:
            res[heappop(V[a])] = a + 1
            while V[a]: heappush(cands, heappop(V[a]))
        else:
            res[heappop(cands)] = a + 1

    return res


def main():
    N = int(input())
    P = list(map(int, input().split()))
    A = list(map(int, input().split()))
    out = solve(N, P, A)
    print(*out)


if __name__ == '__main__':
    main()

