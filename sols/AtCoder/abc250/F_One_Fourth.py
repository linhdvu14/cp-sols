''' F - One Fourth
https://atcoder.jp/contests/abc250/tasks/abc250_f
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

def cross(p, q): return p[0] * q[1] - p[1] * q[0]
def triangle_area2(p, q, r): return abs(cross(p, q) + cross(q, r) + cross(r, p))
def polygon_area2(P, N): return abs(sum(cross(P[i], P[(i+1) % N]) for i in range(N)))


def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    
    res = tar = polygon_area2(P, N) 
    cur = r = 0  # cur is area(l --ccw--> r)
    for l in range(N):
        while cur < tar:
            cur += 4 * triangle_area2(P[l], P[r], P[(r + 1) % N])
            r = (r + 1) % N
            res = min(res, abs(cur - tar))
        cur -= 4 * triangle_area2(P[l], P[(l+1) % N], P[r])
        res = min(res, abs(cur - tar))

    return res



if __name__ == '__main__':
    out = main()
    print(out)

