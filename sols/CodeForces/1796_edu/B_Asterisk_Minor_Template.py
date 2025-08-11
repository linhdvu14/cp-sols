''' B. Asterisk-Minor Template
https://codeforces.com/contest/1796/problem/B
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

def solve(A, B):
    if A[0] == B[0]: return 'YES', A[0] + '*'
    if A[-1] == B[-1]: return 'YES', '*' + A[-1]

    for i in range(len(A) - 1):
        s = A[i:i+2]
        if s in B: return 'YES', '*' + s + '*'

    return 'NO', ''


def main():
    T = int(input())
    for _ in range(T):
        A = input().decode().strip()
        B = input().decode().strip()
        a, b = solve(A, B)
        print(a)
        if b: print(b)


if __name__ == '__main__':
    main()

