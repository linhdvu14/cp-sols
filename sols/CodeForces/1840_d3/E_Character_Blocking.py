''' E. Character Blocking
https://codeforces.com/contest/1840/problem/E
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
from collections import deque

def solve(A, B, D, Q, queries):
    A, B = list(A), list(B)
    diff = sum(1 for a, b in zip(A, B) if a != b)
    block = deque()
    time = 0

    res = []
    for ts in queries:
        if block and block[0][0] == time:
            _, i = block.popleft()
            if A[i] != B[i]: diff += 1
        if ts[0] == 1:
            i = ts[1] - 1
            block.append([time + D, i])
            if A[i] != B[i]: diff -= 1
        elif ts[0] == 2:
            si, sj = ts[1], ts[3]
            i, j = ts[2] - 1, ts[4] - 1
            if A[i] != B[i]: diff -= 1
            if A[j] != B[j]: diff -= 1

            if si == sj == 1: A[i], A[j] = A[j], A[i]
            elif si == sj == 2: B[i], B[j] = B[j], B[i]
            elif si == 1: A[i], B[j] = B[j], A[i]
            else: B[i], A[j] = A[j], B[i]

            if A[i] != B[i]: diff += 1
            if A[j] != B[j]: diff += 1
        else:
            if not diff: res.append('YES')
            else: res.append('NO')

        time += 1
            
    return res


def main():
    T = int(input())
    for _ in range(T):
        A = input().decode().strip()
        B = input().decode().strip()
        D, Q = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(A, B, D, Q, queries)
        print(*res, sep='\n')


if __name__ == '__main__':
    main()

