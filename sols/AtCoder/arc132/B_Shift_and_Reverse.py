''' B - Shift and Reverse
https://atcoder.jp/contests/arc132/tasks/arc132_b
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

def solve(N, A):
    i = A.index(1)
    res = INF
    if A[(i+1)%N] == 2: res = min(res, i, N-i+2)
    if A[(i-1)%N] == 2: res = min(res, i+2, N-i)
    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

