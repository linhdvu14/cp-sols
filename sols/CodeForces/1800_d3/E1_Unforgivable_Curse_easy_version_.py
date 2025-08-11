''' E1. Unforgivable Curse (easy version)
https://codeforces.com/contest/1800/problem/E1
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

def solve(N, K, A, B):
    cnt = [0] * 26
    for i, (a, b) in enumerate(zip(A, B)):
        cnt[ord(a) - ord('a')] += 1
        cnt[ord(b) - ord('a')] -= 1
        if i < K and i > N - K - 1 and a != b: return 'NO'
    
    if all(not c for c in cnt): return 'YES'
    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = input().decode().strip()
        B = input().decode().strip()
        res = solve(N, K, A, B)
        print(res)


if __name__ == '__main__':
    main()

