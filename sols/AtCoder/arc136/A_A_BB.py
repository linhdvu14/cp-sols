''' A - A ↔ BB 
https://atcoder.jp/contests/arc136/tasks/arc136_a
'''

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

def main():
    N = int(input())
    S = input().decode().strip()

    stack = []
    for c in S:
        if c == 'C':
            stack.append(c)
        elif c == 'B':
            if stack and stack[-1] == 'B':
                stack.pop()
                stack.append('A')
            else:
                stack.append('B')
        elif c == 'A':
            if stack and stack[-1] == 'B':
                stack.pop()
                stack.append('A')
                stack.append('B')
            else:
                stack.append('A')
    print(''.join(stack))


if __name__ == '__main__':
    main()

