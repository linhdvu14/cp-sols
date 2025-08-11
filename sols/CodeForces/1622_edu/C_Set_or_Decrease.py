''' C. Set or Decrease
https://codeforces.com/contest/1622/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, K, A):
    S = sum(A)
    if S <= K: return 0

    A.sort()
    res = S - K

    # apply 1st op x times on A[0] then 2nd ops y times on max eles
    # sum result arr is (A[0]-x)*(y+1) + sum(A) - sum(A[-y:]) <= K
    # S = sum(A) - sum(A[-y:])
    S -= A[0]  
    for y in range(1, N):
        S -= A[-y]

        # how much to decrease A[0] to
        m = min(A[0], (K-S) // (y+1) + 1)
        for _ in range(3):
            if S + m*(y+1) <= K:
                x = A[0] - m
                res = min(res, x + y)
                break
            m -= 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

