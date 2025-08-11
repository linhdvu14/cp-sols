''' D. Game on Axis
https://codeforces.com/contest/1787/problem/D
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

def solve(N, A):
    deg = [0] * N 
    goto = [-1] * N
    prev = [[] for _ in range(N)]
    for i, a in enumerate(A):
        j = i + a 
        if 0 <= j < N: 
            deg[j] += 1
            goto[i] = j
            prev[j].append(i)
    
    # upstream tree size
    up = [1] * N 
    st = [u for u in range(N) if not deg[u]]
    while st:
        u = st.pop()
        v = goto[u]
        if v != -1 and deg[v]:
            up[v] += up[u]
            deg[v] -= 1
            if not deg[v]: st.append(v)

    # rm nodes on/leading to cycle
    cyc = 0
    for u in range(N):
        if deg[u]:
            st = [u]
            while st:
                u = st.pop()
                up[u] = 0
                cyc += 1
                st.extend([v for v in prev[u] if not deg[v]])

    # exclude upstream and nodes on/leading to cycle
    res = u = 0
    seen = [0] * N
    while u != -1 and not seen[u]:
        res += 2 * N + 1 - up[u] - cyc 
        seen[u] = 1
        u = goto[u]
    if u == -1: res += (2 * N + 1) * (N - sum(seen))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

