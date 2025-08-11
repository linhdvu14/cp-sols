''' B - KEYENCE building
https://atcoder.jp/contests/abc227/tasks/abc227_b
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

# (4a + 3)(4b + 3) = 4S + 9

def main():
    N = int(input())
    S = list(map(int, input().split()))

    res = 0
    for s in S:
        s = 4 * s + 9
        bad = 1
        for a in range(1, s // 7 + 10):
            for b in range(1, a + 1):
                if (4*a + 3) * (4*b + 3) == s:
                    bad = 0
                    break
        res += bad

    return res


if __name__ == '__main__':
    res = main()
    print(res)

