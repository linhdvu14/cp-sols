''' C. Factorials and Powers of Two
https://codeforces.com/contest/1646/problem/C
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

FACT = [6]
for i in range(4, 16): FACT.append(FACT[-1] * i)

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

def solve(N):
    @bootstrap
    def dfs(n, i=0):
        if n < 0: yield INF
        if n == 0: yield 0
        if i == len(FACT): yield bin(n).count('1')
        l = yield dfs(n - FACT[i], i+1)
        r = yield dfs(n, i+1)
        yield min(1 + l, r)

    return dfs(N)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

