''' Problem 1. Searching for Soulmates '''

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


@bootstrap
def dfs(x, y, memo):
    if x == y: yield 0
    if (x, y) in memo: yield memo[x, y]
    rx, ry = x, y

    res = 0
    while x > y and x % 2 == 0:
        x >>= 1
        res += 1
    
    if x == y: 
        memo[rx, ry] = res
    elif x > y:  # x % 2 == 1
        t = yield dfs(x+1, y, memo)
        memo[rx, ry] = res + 1 + t
    else:
        add = y - x
        d = y.bit_length() - x.bit_length()
        if (y >> d) == x:  # x is prefix of y
            add = min(add, d + bin(y)[-d:].count('1'))
        elif x % 2 == 1:
            t = yield dfs(x+1, y, memo)
            add = min(add, 1 + t)
        else:
            t1 = yield dfs(x >> 1, y, memo)
            t2 = yield dfs(x + 1, y, memo)
            add = min(add, 1 + t1, 1 + t2)
        memo[rx, ry] = res + add
    yield memo[rx, ry]


def main():
    N = int(input())
    memo = {}
    for _ in range(N):
        x, y = list(map(int, input().split()))
        out = dfs(x, y, memo)
        print(out)
        break


if __name__ == '__main__':
    main()