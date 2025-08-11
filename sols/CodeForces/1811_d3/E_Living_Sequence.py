''' E. Living Sequence
https://codeforces.com/contest/1811/problem/E
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

MAP = [0, 1, 2, 3, 5, 6, 7, 8, 9]

def solve(k):
    digits = []
    while k:
        k, d = divmod(k, 9)
        digits.append(MAP[d])
    digits.reverse()
    res = ''.join(map(str, digits))
    return res


def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        res = solve(k)
        print(res)


if __name__ == '__main__':
    main()

