''' B. 3-Coloring
https://codeforces.com/contest/1503/problem/B
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

class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)

INF = float('inf')

# -----------------------------------------

# place a on W and b on B, until all W's or all B's are filled, say W
# then fill remaining B's with b if Alice chooses a or j, or j of Alice chooses b

def main():
    N = int(input())

    slots = [[], []]
    for i in range(N):
        for j in range(N):
            slots[(i + j) % 2].append((i + 1, j + 1))

    x = int(input())
    a = 1 if x != 1 else 2
    i, j = slots[0].pop()
    output(a, i, j)

    x = int(input())
    b = list({1, 2, 3} - {a, x})[0]
    i, j = slots[1].pop()
    output(b, i, j)

    c = list({1, 2, 3} - {a, b})[0]

    while slots[0] and slots[1]:
        x = int(input())
        if x == a: 
            i, j = slots[1].pop()
            output(b, i, j)
        else:
            i, j = slots[0].pop()
            output(a, i, j) 
    
    while slots[0]:  # fill with a and c
        x = int(input())
        i, j = slots[0].pop()
        if x == a: output(c, i, j)
        else: output(a, i, j)
    
    while slots[1]:  # fill with b and c
        x = int(input())
        i, j = slots[1].pop()
        if x == b: output(c, i, j)
        else: output(b, i, j)    

    
 
if __name__ == '__main__':
    main()