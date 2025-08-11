''' D - Project Planning
https://atcoder.jp/contests/abc227/tasks/abc227_d
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

from bisect import bisect_left

def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()

    pref = [0]
    for a in A: pref.append(pref[-1] + a)

    # distribute all groups with size >= n, 1 member per each of n projects
    # then interleave all groups with size < n
    def is_ok(n):
        i = bisect_left(A, n)
        rem = (K - N + i) * n 
        return rem <= pref[i]
    
    res, lo, hi = 0, 0, sum(A) // K
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi 
            lo = mi + 1
        else:
            hi = mi - 1
    
    return res




if __name__ == '__main__':
    res = main()
    print(res)

