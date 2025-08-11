''' Suspects and Witnesses
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76db9
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

def solve(N, M, K, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:  # reverse edge
        adj[v-1].append(u-1)

    # if num unique v reachable from u > K, then u must be innocent
    def is_ok(u):
        seen = set([u])
        stack = [u]
        while stack:
            if len(seen) > K: return True
            u = stack.pop()
            for v in adj[u]:
                if v in seen: continue
                seen.add(v)
                stack.append(v)
        return False
    
    res = sum(1 for u in range(N) if is_ok(u))
    return res
    


def main():
    T = int(input())
    for t in range(T):
        N, M, K = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        out = solve(N, M, K, edges)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

