''' D. Sakurako's Hobby
https://codeforces.com/contest/2008/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']
DEBUG_CASE = int(os.environ.get('case', 0))

def debug(*args):   
    if not DEBUG: return
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

def solve(N, P, S):
    vis = [0] * N
    res = [0] * N

    for u in range(N):
        path = []
        cnt = 0
        while not vis[u]:
            path.append(u)
            vis[u] = 1
            cnt += S[u] == '0'
            u = P[u] - 1
        for u in path: res[u] = cnt

    return res


def main():
    T = int(input())
    for ti in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        S = input().decode().strip()
        if DEBUG and DEBUG_CASE and ti != DEBUG_CASE: continue
        res = solve(N, P, S)
        print(*res)


if __name__ == '__main__':
    main()

