''' B - Perfect String
https://atcoder.jp/contests/abc249/tasks/abc249_b
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

from string import ascii_lowercase, ascii_uppercase

def main():
    S = input().decode().strip()
    if all(c not in S for c in ascii_lowercase): print('No')
    elif all(c not in S for c in ascii_uppercase): print('No')
    elif len(S) != len(set(S)): print('No')
    else: print('Yes')



if __name__ == '__main__':
    main()

