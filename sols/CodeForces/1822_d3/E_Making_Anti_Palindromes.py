''' E. Making Anti-Palindromes
https://codeforces.com/contest/1822/problem/E
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
from string import ascii_lowercase

def solve(N, S):
    mx = max(S.count(c) for c in ascii_lowercase)
    if N % 2 or mx > N // 2: return -1

    cnt = [0] * 26
    for i in range(N // 2):
        if S[i] == S[N - 1 - i]:
            cnt[ord(S[i]) - ord('a')] += 1

    return max(max(cnt), (sum(cnt) + 1) // 2)
    


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        res = solve(N, S)
        print(res)


if __name__ == '__main__':
    main()

