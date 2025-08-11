''' Triple Inversions 
https://www.codechef.com/COOK141A/problems/TRIPLE_INVS
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


def solve(N, A):
    @bootstrap
    def dfs(i, l=-1, m=-1):
        if i == N: yield True
        if A[i] == 0: choices = [(1, 2, 3)]
        elif A[i] == 1: choices = [(1, 3, 2), (2, 1, 3)]
        elif A[i] == 2: choices = [(2, 3, 1), (3, 1, 2)]
        else: choices = [(3, 2, 1)]
        ok = False
        for nl, nm, nr in choices:
            if l != -1 and (nl < nm) != (l < m): continue
            ok |= yield dfs(i+1, nm, nr)
        yield ok

    return dfs(0)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

