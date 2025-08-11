''' C. Sum on Subarrays
https://codeforces.com/contest/1809/problem/C
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

def solve(N, K):
    pos = [0] * N
    for i in range(N - 1, -1, -1):
        if i + 1 <= K:
            pos[i] = 1
            K -= i + 1

    mn = mx = s = 0
    res = [0] * N
    for i, p in enumerate(pos):
        if p: res[i] = mx + 1 - s
        else: res[i] = mn - 1 - s
        s += res[i]
        mn = min(mn, s)
        mx = max(mx, s)
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        res = solve(N, K)
        print(*res)


if __name__ == '__main__':
    main()

