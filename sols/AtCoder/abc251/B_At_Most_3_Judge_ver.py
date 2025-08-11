''' B - At Most 3 (Judge ver.)
https://atcoder.jp/contests/abc251/tasks/abc251_b
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
    N, W = list(map(int, input().split()))
    A = list(map(int, input().split()))

    ok = [0] * (W + 1)
    for i, a in enumerate(A):
        if a <= W: ok[a] = 1
        for j in range(i):
            b = A[j]
            if a + b <= W: ok[a + b] = 1
            for k in range(j):
                c = A[k]
                if a + b + c <= W: ok[a + b + c] = 1
    
    return sum(ok)



if __name__ == '__main__':
    res = main()
    print(res)

