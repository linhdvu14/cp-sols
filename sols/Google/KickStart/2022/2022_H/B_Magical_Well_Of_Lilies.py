''' Magical Well Of Lilies 
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47e79
'''

import os, sys
input = sys.stdin.readline
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


def solve(N):
    @bootstrap
    def dfs(a, memo={}):
        if a == 0: yield 1 + (yield dfs(1, memo))
        if a >= N: yield 0
        if a * 2 > N: yield N - a
        if a * 2 == N: yield min(N - a, 6)
        if a in memo: yield memo[a]

        res = 1 + (yield dfs(a + 1, memo))
        for i in range(1, N // a):
            res = min(res, 4 + 2 * i + (yield dfs(a * (i + 1), memo)))

        memo[a] = res 
        yield res

    return dfs(0)


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        res = solve(N)
        print(f'Case #{t+1}: {res}')


def gen():
    import random
    random.seed(123)

    for _ in range(100):
        N = random.randint(1, 100)
        print(N)
        solve(N)
    print('tests passed')



if __name__ == '__main__':
    main()
    # gen()

