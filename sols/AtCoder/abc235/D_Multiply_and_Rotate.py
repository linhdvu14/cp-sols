''' D - Multiply and Rotate
https://atcoder.jp/contests/abc235/tasks/abc235_d
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

from heapq import heappush, heappop

def main():
    a, N = list(map(int, input().split()))

    dist = {}
    h = [(0, N)]
    while h:
        d, x = heappop(h)
        if x == 1: return d

        if dist.get(x, INF) <= d: continue
        dist[x] = d

        d += 1
        if x % a == 0 and dist.get(x // a, INF) > d: heappush(h, (d, x // a))

        y = str(x)
        if len(y) > 1 and y[1] != '0':
            y = int(y[1:] + y[0])
            if dist.get(y, INF) > d: heappush(h, (d, y))

    return -1


if __name__ == '__main__':
    res = main()
    print(res)

