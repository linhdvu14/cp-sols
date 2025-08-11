''' Problem A: Second Hands
https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/A
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

def solve(N, K, A):
    if 2 * K < N: return 'NO'

    cnt = {}
    for a in A: 
        cnt[a] = cnt.get(a, 0) + 1
        if cnt[a] > 2: return 'NO'
    
    return 'YES'


def main():
    T = int(input())
    for t in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()

