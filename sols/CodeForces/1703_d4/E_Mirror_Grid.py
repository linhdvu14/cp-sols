''' E. Mirror Grid
https://codeforces.com/contest/1703/problem/E
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


class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)


INF = float('inf')

# -----------------------------------------

def solve(N, grid):
    res = 0
    for i in range(N//2):
        for c in range(i, N-i-1):
            r = i
            ones = 0
            for _ in range(4):
                if grid[r][c] == '1': ones += 1
                r, c = c, N-1-r
            res += min(ones, 4 - ones)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input().decode().strip() for _ in range(N)]
        out = solve(N, grid)
        print(out)


if __name__ == '__main__':
    main()

