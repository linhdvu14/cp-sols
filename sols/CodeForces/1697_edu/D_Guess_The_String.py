''' D. Guess The String
https://codeforces.com/contest/1697/problem/D
'''

# to test: 
# pypy3 template.py
# or: python3 interactive_runner.py python3 local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

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

def ask(s):
    output(s)
    res = input().strip()
    return res


def main():
    N = int(input())

    res = [''] * N
    for i in range(N):
        if i == 0:
            res[i] = ask('? 1 1')
        else:
            last = {res[j]: j for j in range(i)}
            last = sorted([(j, c) for c, j in last.items()], reverse=True)

            # search for max j s.t. S[j..i] includes S[i]
            idx, lo, hi = -1, 0, len(last) - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                ln = int(ask(f'? 2 {last[mi][0] + 1} {i+1}'))
                if ln == mi + 1:
                    idx = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            
            if idx == -1: res[i] = ask(f'? 1 {i+1}')
            else: res[i] = last[idx][1]
    
    res = ''.join(res)
    ask(f'! {res}')


 
if __name__ == '__main__':
    main()
