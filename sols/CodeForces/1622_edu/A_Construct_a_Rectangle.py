''' A. Construct a Rectangle
https://codeforces.com/contest/1622/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(a, b, c):
    if a==b+c or b==a+c or c==a+b: return True
    if (a%2==0 and b==c) or (b%2==0 and c==a) or (c%2==0 and a==b): return True
    return False


def main():
    T = int(input())
    for _ in range(T):
        a, b, c = list(map(int, input().split()))
        out = solve(a, b, c)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

