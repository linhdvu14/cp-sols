''' Problem 1. Redistributing Gifts 
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

from collections import deque

def main():
    N = int(input())

    perms = []
    for _ in range(N):
        p = map(int, input().split())
        p = [x-1 for x in p]
        perms.append(p)

    # inv_perms[i][j] = cow i's rank of gift j
    # want inv_perms[i][j] < inv_perms[i][i]
    inv_perms = []
    for p in perms:
        ip = [-1] * N
        for i, x in enumerate(p):
            ip[x] = i
        inv_perms.append(ip)

    # extend[i] = all cows j that wants gift i
    extend = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if inv_perms[j][i] < inv_perms[j][j]:
                extend[i].append(j)

    for i in range(N):
        q = deque([i])
        used = [0]*N
        used[i] = 1
        # bfs until set unchanged
        while q:
            u = q.popleft()
            for v in extend[u]:
                if not used[v]: 
                    q.append(v)
                    used[v] = 1
        # give cow i best gift receivable
        for j in perms[i]:
            if used[j]:
                print(j+1)
                break


if __name__ == '__main__':
    main()