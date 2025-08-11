''' B - Enlarged Checker Board
https://atcoder.jp/contests/abc250/tasks/abc250_b
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
    N, A, B = list(map(int, input().split()))
    w, b = '.' * B, '#' * B 
    wr = ''.join(w if i % 2 == 0 else b for i in range(N))
    br = ''.join(w if i % 2 == 1 else b for i in range(N))
    for i in range(N):
        for _ in range(A):
            if i % 2 == 0: print(wr)
            else: print(br)

if __name__ == '__main__':
    main()

