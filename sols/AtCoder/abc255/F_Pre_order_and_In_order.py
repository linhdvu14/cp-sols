''' F - Pre-order and In-order
https://atcoder.jp/contests/abc255/tasks/abc255_f
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


def main():
    N = int(input())
    P = list(map(int, input().split()))
    I = list(map(int, input().split()))

    if P[0] != 1: return [[-1]]

    pos = {a: i for i, a in enumerate(I)}
    L, R = [0] * N, [0] * N

    @bootstrap
    def dfs(il, ir, pl, pr):
        # subtree root and idx in I
        root = P[pl]
        idx = pos[root]

        if not il <= idx <= ir: yield -1
        
        # num nodes in left/right subtree
        nl = idx - il
        nr = ir - il - nl

        if nl: L[root-1] = yield dfs(il, il+nl-1, pl+1, pl+nl)
        if nr: R[root-1] = yield dfs(idx+1, ir, pl+nl+1, pr)

        yield root
    
    if dfs(0, N-1, 0, N-1) == -1: return [[-1]]
    if -1 in L or -1 in R: return [[-1]]
    return list(zip(L, R))


if __name__ == '__main__':
    out = main()
    for tup in out: print(*tup)

