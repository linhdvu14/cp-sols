''' D2. Red-Blue Operations (Hard Version)
https://codeforces.com/contest/1832/problem/D2
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

def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    
    A.sort()
    idx = {k: i for i, k in enumerate(queries) if k <= N}
    res = [-1] * Q 

    # k <= N
    mn = INF
    for k in range(1, N + 1):
        mn = min(mn, A[k - 1]) + 1
        if k in idx:
            if k < N: res[idx[k]] = min(mn, A[k])
            else: res[idx[k]] = mn

    # k > N
    tot = [0, 0]
    base = [INF, INF]
    for i, a in enumerate(A):
        b = a + N - i 
        tot[0] += b
        base[0] = min(base[0], b)
        if i < N - 1:
            tot[1] += b 
            base[1] = min(base[1], b)
        else:
            tot[1] += a

    for i, k in enumerate(queries):
        if res[i] != -1: continue
        if k % 2 == N % 2:
            mn = base[0] + k - N 
            free = tot[0] + (k - N) * N - mn * N
        else:
            mn = min(base[1] + k - N, A[-1])
            free = tot[1] + (k - N) * (N - 1) - mn * N
        sub = (k + 1 - N) // 2
        rem = max(0, sub - free)
        res[i] = mn - rem // N - (1 if rem % N else 0)

    print(*res)


if __name__ == '__main__':
    main()

