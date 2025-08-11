''' Yet Another Contest 4 P2 - Alchemy 2
https://dmoj.ca/problem/yac4p2
'''

import os, sys
from re import I
input = sys.stdin.readline  # strip() if str

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

def solve(N, B):
    res = [-1] * N
    ptr = [-1] * (N + 1)
    idx = sorted(list(range(N)), key=lambda i: B[i], reverse=True)
    while idx:
        i = idx.pop()
        if B[i] == 1:
            res[i] = ptr[1] = i + 1
        elif ptr[B[i] - 1] != -1:
            res[i] = ptr[B[i] - 1]
            ptr[B[i]] = i + 1
        else:
            cur = [i]
            while len(cur) < B[i] and idx and B[idx[-1]] == B[i]: cur.append(idx.pop())
            if len(cur) < B[i]: return [-1]
            for k in range(len(cur)): res[cur[k]] = cur[(k + 1) % len(cur)] + 1
            ptr[B[i]] = cur[0] + 1
    return res



def main():
    N = int(input())
    B = list(map(int, input().split()))
    out = solve(N, B)
    print(*out)


if __name__ == '__main__':
    main()

