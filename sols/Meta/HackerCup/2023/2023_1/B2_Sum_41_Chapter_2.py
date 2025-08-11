''' Problem B2: Sum 41 (Chapter 2)
https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B2
'''

import os, sys
input = sys.stdin.readline  # strip() if str
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
    T = int(input())

    PMAX = 10**9
    MEMO = {}

    @bootstrap
    def dfs(s, mn, p, ls=[]):
        if s == 0:
            if p not in MEMO or len(MEMO[p]) > len(ls):
                MEMO[p] = ls
        elif mn <= s:
            yield dfs(s, mn + 1, p, ls)
            if p * mn <= PMAX: yield dfs(s - mn, mn, p * mn, ls + [mn])
        yield None

    dfs(41, 1, 1, [])

    for t in range(T):
        P = int(input())
        if P in MEMO: print(f'Case #{t + 1}: {len(MEMO[P])}', *MEMO[P])
        else: print(f'Case #{t + 1}: -1')
    

if __name__ == '__main__':
    main()

