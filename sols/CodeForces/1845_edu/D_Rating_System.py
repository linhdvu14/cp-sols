''' D. Rating System
https://codeforces.com/contest/1845/problem/D
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

def solve_1(N, A):
    ps = [0] * (N + 1)
    for i, a in enumerate(A): ps[i + 1] = ps[i] + a 

    # next_leq[i] = min j > i s.t. ps[j] <= ps[i]
    next_leq = [-1] * (N + 1)
    st = []
    for i in range(N, -1, -1):
        while st and ps[st[-1]] > ps[i]: st.pop()
        if st: next_leq[i] = st[-1]
        st.append(i)

    # dp[i] = final score on A[i..], if start at 0 and do not dip below 0
    dp = [0] * (N + 1)
    res = (-INF, -INF)
    for i in range(N, -1, -1):
        j = next_leq[i]
        if j == -1: dp[i] = ps[-1] - ps[i]
        else: dp[i] = dp[j]
        res = max(res, (ps[i] + dp[i], ps[i]))

    return res[1]


def solve_2(N, A):
    mx = ps = 0
    res = (INF, INF)
    for a in A:
        ps += a 
        res = min(res, (ps - mx, mx))
        mx = max(mx, ps)
    return res[1]


solve = solve_2


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()
