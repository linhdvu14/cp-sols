''' E - Minimal payments
https://atcoder.jp/contests/abc231/tasks/abc231_e
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


# X = c[0] * a[0] + c[1] * a[1] + c[2] * a[2] + ...
# need to min sum abs(c[i])

def main():
    N, X = list(map(int, input().split()))
    A = list(map(int, input().split()))

    @bootstrap
    def dfs(x, i=0, memo={}):
        if x == 0 or i == N: yield 0
        if i == N-1: yield x // A[i]
        if (x, i) in memo: yield memo[x, i]
        a = x % A[i + 1]  # amount to be changed with A[i]
        memo[x, i] = min(
            a // A[i] + (yield dfs(x - a % A[i], i+1, memo)),  # round down
            A[i+1] // A[i] - a // A[i] + (yield dfs(x - a % A[i] + A[i+1], i+1, memo)),  # round up
        )
        yield memo[x, i]

    res = dfs(X)    
    print(res)



if __name__ == '__main__':
    main()

