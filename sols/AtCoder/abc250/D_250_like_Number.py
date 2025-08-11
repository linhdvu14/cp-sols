''' D - 250-like Number
https://atcoder.jp/contests/abc250/tasks/abc250_d
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

from bisect import bisect_right

def main():
    N = int(input())

    primes = [2, 3, 5, 7]
    for n in range(9, int(pow(N, 1/3)) + 1, 2):
        d = 3
        ok = True
        while d * d < n:
            if n % d == 0:
                ok = False
                break
            d += 1
        if n % d == 0: ok = False
        if ok: primes.append(n)
    
    res = 0
    for i in range(1, len(primes)):
        res += min(i, bisect_right(primes, N // (primes[i] ** 3)))
    
    return res



if __name__ == '__main__':
    out = main()
    print(out)

