''' E - Takahashi and Animals
https://atcoder.jp/contests/abc251/tasks/abc251_e
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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc

INF = float('inf')

# -----------------------------------------

def solve_1(N, A):
    # dp[0/1][i] = min cost to cover 0..i, with edge (i, i+1) not chosen/chosen
    # choose edge (0, 1), then edge (N-1, 0) can be chosen or not chosen
    dp = [[INF] * N for _ in range(2)]
    dp[1][0] = A[0]
    for i in range(1, N):
        dp[0][i] = dp[1][i-1]
        dp[1][i] = A[i] + min(dp[0][i-1], dp[1][i-1])
    res = min(dp[0][N-1], dp[1][N-1])

    # do not choose edge (0, 1), then edge (N-1, 0) must be chosen
    dp = [[INF] * N for _ in range(2)]
    dp[0][0] = 0
    for i in range(1, N):
        dp[0][i] = dp[1][i-1]
        dp[1][i] = A[i] + min(dp[0][i-1], dp[1][i-1])
    res = min(res, dp[1][N-1])

    return res


def solve_2(N, A):
    def solve_linear(A):
        # dp[i] = min cost to cover A[:i]
        dp = [INF] * (len(A) + 1)
        dp[0] = 0
        for i in range(len(A)):
            dp[i + 1] = dp[i] + A[i]  # select (i, i+1)
            if i: dp[i + 1] = min(dp[i + 1], dp[i - 1] + A[i - 1])  # do not select (i, i+1), must select (i-1, i) and cover A[0..i-2]
        return dp[-1]

    return min(solve_linear(A), solve_linear(A[1:-1]) + A[-1])


solve = solve_2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    print(res)


if __name__ == '__main__':
    main()

