''' C. Insert Zero and Invert Prefix
https://codeforces.com/contest/1839/problem/C
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

def solve(N, A):
    if A[-1] == 1: return 'NO', []

    res = []
    while A:
        one = zero = 0
        while A and A[-1] == 0:
            zero += 1
            A.pop()
        while A and A[-1] == 1:
            one += 1
            A.pop()
        res += [0] * (one + zero - 1) + [one]

    return 'YES', res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        a, b = solve(N, A)
        print(a)
        if b: print(*b)


if __name__ == '__main__':
    main()

