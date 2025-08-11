''' B. Vika and the Bridge
https://codeforces.com/contest/1848/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

def solve(N, K, A):
    dist = [[] for _ in range(K)]
    prev = [-1] * K
    for i, a in enumerate(A):
        a -= 1
        dist[a] = sorted(dist[a] + [i - prev[a] - 1], reverse=True)[:2]
        prev[a] = i

    res = INF
    for a in range(K):
        if prev[a] == -1: continue
        dist[a] = sorted(dist[a] + [N - prev[a] - 1], reverse=True)[:2]
        mx = dist[a][0] // 2
        if len(dist[a]) > 1: mx = max(mx, dist[a][1])
        res = min(res, mx)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(res)


if __name__ == '__main__':
    main()

