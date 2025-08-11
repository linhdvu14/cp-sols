''' E. Replace With the Previous, Minimize
https://codeforces.com/contest/1675/problem/E
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

def solve(N, K, S):
    S = [ord(c) - ord('a') for c in S]
    res = []
    mx = 0
    for i in range(N):
        if S[i] <= K:
            res.append(0)
            mx = max(mx, S[i])
        else:
            K -= mx
            for j in range(i, N):
                if S[j] <= mx: res.append(0)
                elif S[i] - K <= S[j] <= S[i]: res.append(S[i] - K)
                else: res.append(S[j])
            break

    return ''.join(chr(ord('a') + c) for c in res)


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        S = input().decode().strip()
        out = solve(N, K, S)
        print(out)


if __name__ == '__main__':
    main()

