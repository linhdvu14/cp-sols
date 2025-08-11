''' D. The Enchanted Forest
https://codeforces.com/contest/1688/problem/D
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

# after K steps, total new mushrooms are K * N
# should minimize number of uncollected mushrooms
# can collect at most i mushrooms (leave at least N - i) at step K - i
def solve_1(N, K, A):
    if K <= N:
        mx = s = sum(A[:K])
        for i in range(K, N):
            s += A[i] - A[i - K]
            mx = max(mx, s)
        return mx + K * (K - 1) // 2
    return sum(A) + K * N - N * (N + 1) // 2
    

# best to avoid repeating points
# if K <= N, should visit max sum subarray of length K
# else should bounce off some initial starting point, i.e. i -> N-1 -> 0 -> N-1 ...
def solve_2(N, K, A):
    if N == 1: return A[0] + K - 1
    if K <= N:
        mx = s = sum(A[:K])
        for i in range(K, N):
            s += A[i] - A[i - K]
            mx = max(mx, s)
        return mx + K * (K - 1) // 2
    
    # scores for starting at 0 and going 0 -> N-1 -> 0 -> N-1 for d steps
    def f(d):
        assert d >= 0
        n, r = divmod(d, N - 1)
        return n * N * (N - 1) + r * (r + 1)

    # try each possible i
    res = 0
    for i in range(N):
        s, rem = 0, K

        # i -> 0
        s += i * (i + 1) // 2
        rem -= i + 1

        # 1 -> i
        d = min(rem, i)
        s += d * (d + 1)
        rem -= d

        # i+1 -> N-1
        d = min(rem, N - i - 1)
        s += d * (d - 1) // 2 + d * (2 * i + 1)
        rem -= d

        # bounce
        s += f(rem)

        res = max(res, s)
    
    return res + sum(A)


solve = solve_1

def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        print(out)


if __name__ == '__main__':
    main()

