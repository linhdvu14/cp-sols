''' Excalibur
https://www.codechef.com/ENCO2022/problems/ENCOD04
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


BITS = 60

# dp[i][prev][free]
dp = [[[-1]*2 for _ in range(2)] for _ in range(BITS)]

def count_leq(N):
    for i in range(N.bit_length()):
        for j in range(2):
            for k in range(2):
                dp[i][j][k] = -1

    @bootstrap
    def dfs(i, prev=0, free=0):  # build i-th digit
        if i < 0: yield 1
        if dp[i][prev][free] != -1: yield dp[i][prev][free]
        res = yield dfs(i-1, 0, free or (N>>i) & 1)
        if prev != 1 and (free | (N>>i) & 1): res += yield dfs(i-1, 1, free)
        dp[i][prev][free] = res
        yield res

    return dfs(N.bit_length() - 1)


def solve(L, R):
    return count_leq(R) - count_leq(L-1)


def main():
    T = int(input())
    for _ in range(T):
        L, R = list(map(int, input().split()))
        out = solve(L, R)
        print(out)


if __name__ == '__main__':
    main()

