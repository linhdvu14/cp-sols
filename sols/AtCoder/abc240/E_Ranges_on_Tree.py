''' E - Ranges on Tree
https://atcoder.jp/contests/abc240/tasks/abc240_e
'''

from curses import nonl
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


def main():
    N = int(input())

    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    res = [None] * N

    @bootstrap
    def postorder(u, p=-1, start=1):
        end = start
        for v in adj[u]:
            if v == p: continue
            end = yield postorder(v, u, end)
            end += 1
        if len(adj[u]) > 1 or p == -1: end -= 1
        res[u] = (start, end)
        yield end

    postorder(0)
    for v in res: print(*v)



if __name__ == '__main__':
    main()

