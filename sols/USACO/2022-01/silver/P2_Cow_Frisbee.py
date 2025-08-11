''' Problem 2. Cow Frisbee '''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

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


INF = float('inf')

# -----------------------------------------

def solve(N, A):
    res = 0

    # count (i, j) where A[i] < A[j]
    stack = []
    for i, a in enumerate(A):
        while stack and A[stack[-1]] < a: stack.pop()
        if stack: res += i - stack[-1] + 1
        stack.append(i)

    # count (i, j) where A[i] > A[j]
    A.reverse()
    stack = []
    for i, a in enumerate(A):
        while stack and A[stack[-1]] < a: stack.pop()
        if stack: res += i - stack[-1] + 1
        stack.append(i)
    
    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

