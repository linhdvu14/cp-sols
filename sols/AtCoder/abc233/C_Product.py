''' C - Product
https://atcoder.jp/contests/abc233/tasks/abc233_c
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

def main():
    N, X = list(map(int, input().split()))
    balls = [list(map(int, input().split()))[1:] for _ in range(N)]

    res = 0

    @bootstrap
    def dfs(i, prod=1):
        nonlocal res
        if i == N and prod == X: res += 1
        elif i < N:
            for b in balls[i]:
                yield dfs(i + 1, prod * b)
        yield None
    
    dfs(0)
    return res
    




if __name__ == '__main__':
    res = main()
    print(res)

