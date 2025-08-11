''' Yet Another Contest 2 P2 - Secret Sequence
https://dmoj.ca/problem/yac2p2
'''

# to test: 
# pypy3 template.py
# or: python3 interactive_runner.py python3 local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

INF = float('inf')

# -----------------------------------------

def ask(l, r):
    output(f'? {l+1} {r+1}')
    res = int(input())
    assert res != -1
    return res


def main():
    N = int(input())
    tot = ask(0, N-1)
    left, right = [], []

    if N % 2 == 0:
        prev = tot
        for r in range(N-2, (N-1)//2 - 1, -1):
            cur = ask(0, r)
            right.append(prev ^ cur)
            prev = cur
        prev = tot
        for l in range(1, (N+1)//2 + 1):
            cur = ask(l, N-1)
            left.append(prev ^ cur)
            prev = cur
        output(f'! {" ".join(list(map(str, left + right[::-1])))}')
    else:
        prev = tot
        for r in range(N-2, (N-1)//2 - 1, -1):
            cur = ask(0, r)
            right.append(prev ^ cur)
            prev = cur
        prev = tot
        for l in range(1, (N-1)//2 + 1):
            cur = ask(l, N-1)
            left.append(prev ^ cur)
            prev = cur
        mid = tot
        for a in left: mid ^= a
        for a in right: mid ^= a
        output(f'! {" ".join(list(map(str, left + [mid]+ right[::-1])))}')


if __name__ == '__main__':
    main()
