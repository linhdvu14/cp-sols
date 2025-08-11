''' C. Binary String Copying
https://codeforces.com/contest/1849/problem/C
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

def solve(N, M, S, segs):
    # nxt[i] = min j >= i s.t. S[j] = 1
    nxt = [N] * (N + 1)
    for i in range(N - 1, -1, -1):
        if S[i] == 1: nxt[i] = i 
        else: nxt[i] = nxt[i + 1]

    # prv[i] = max j <= i s.t. S[j] = 0
    prv = [-1] * (N + 1)
    for i in range(N):
        if S[i] == 0: prv[i] = i 
        else: prv[i] = prv[i - 1]
    
    res = set()
    for l, r in segs:
        l = nxt[l - 1]
        r = prv[r - 1]
        if l > r: res.add((-1, -1))
        else: res.add((l, r))

    return len(res)


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        S = list(map(int, list(input().decode().strip())))
        segs = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, S, segs)
        print(res)


if __name__ == '__main__':
    main()

