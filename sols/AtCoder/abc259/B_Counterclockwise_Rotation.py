''' B - Counterclockwise Rotation
https://atcoder.jp/contests/abc259/tasks/abc259_b
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

from math import sin, cos, radians

def main():
    a, b, d = list(map(int, input().split()))
    d = radians(d)
    a2 = cos(d) * a - sin(d) * b 
    b2 = sin(d) * a + cos(d) * b
    return a2, b2


if __name__ == '__main__':
    out = main()
    print(*out)

