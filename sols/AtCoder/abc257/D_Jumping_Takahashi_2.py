''' D - Jumping Takahashi 2
https://atcoder.jp/contests/abc257/tasks/abc257_d
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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


def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    
    cost = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i):
            x1, y1, p1 = points[i]
            x2, y2, p2 = points[j]
            d = abs(x1 - x2) + abs(y1 - y2)
            cost[i][j] = (d + p1 - 1) // p1
            cost[j][i] = (d + p2 - 1) // p2
    
    def is_ok(s):
        @bootstrap
        def dfs(u):
            seen[u] = 1
            for v in range(N):
                if seen[v]: continue
                if s < cost[u][v]: continue
                yield dfs(v)
            yield None

        for u in range(N):
            seen = [0] * N
            dfs(u)
            if sum(seen) == N: return True
        return False

    res, lo, hi = -1, 0, max(max(row) for row in cost)
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi
            hi = mi - 1
        else:
            lo = mi + 1
    
    print(res)


if __name__ == '__main__':
    main()

