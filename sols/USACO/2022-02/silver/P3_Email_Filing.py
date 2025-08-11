''' Problem 3. Email Filing
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

from collections import deque

def solve(M, N, K, E):
    # count remain of each type
    E = [e-1 for e in E]
    cnt = [0] * M
    for e in E: cnt[e] += 1

    # current folder and emails
    f = 0
    while f < M and cnt[f] == 0: f += 1

    right, left = deque([]), deque([])
    for e in E:
        if len(right) >= K:
            left.append(right.popleft())
        if f <= e < f + K:
            cnt[e] -= 1
            while f < M and cnt[f] == 0: 
                f += 1
                for e in right:
                    if f <= e < f + K:
                        cnt[e] -= 1
                right = deque([e for e in right if not f <= e < f + K])
        else:
            right.append(e)
    
    # handle left
    while f < M and cnt[f] == 0: 
        f += 1
        for e in right:
            if f <= e < f + K:
                cnt[e] -= 1
        right = deque([e for e in right if not f <= e < f + K])
    
    while left:
        if len(right) >= K: return False
        e = left.pop()
        if f <= e < f + K:
            cnt[e] -= 1
            while f < M and cnt[f] == 0: 
                f += 1
                for e in right:
                    if f <= e < f + K:
                        cnt[e] -= 1
                right = deque([e for e in right if not f <= e < f + K])
        else:
            right.appendleft(e)

    return len(right) == 0


def main():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        E = list(map(int, input().split()))
        out = solve(M, N, K, E)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()


