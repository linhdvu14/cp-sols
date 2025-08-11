''' C. Unlucky Numbers
https://codeforces.com/contest/1808/problem/C
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


def solve(L, R):
    R = list(map(int, list(R)))
    L = list(map(int, list(L)))
    if len(L) < len(R): return '9' * len(L)
    N = len(L)

    # whether can create a number with all digits in range lo..hi
    @bootstrap
    def f(i, lo, hi, s='', free_l=False, free_r=False):
        if i == N: yield s
        l, r = lo, hi
        if not free_l: l = max(l, L[i])
        if not free_r: r = min(r, R[i])
        if l > r: yield ''
        if r - l > 1: yield s + str(l + 1) * (N - i)
        n = yield f(i + 1, lo, hi, s + str(l), free_l or l > L[i], free_r or l < R[i])
        if not n and l + 1 == r: n = yield f(i + 1, lo, hi, s + str(r), free_l or r > L[i], free_r or r < R[i])
        yield n
    
    res = (INF, '')
    for lo in range(10):
        for hi in range(lo, 10):
            s = f(0, lo, hi)
            if s: res = min(res, (hi - lo, s))
    
    return res[1]


def main():
    T = int(input())
    for _ in range(T):
        L, R = input().decode().strip().split()
        res = solve(L, R)
        print(res)




if __name__ == '__main__':
    main()

