''' Problem B: Dim Sum Delivery
https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/B
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

def solve(R, C, A, B):
    return 'YES' if R > C else 'NO'


def main():
    T = int(input())
    for t in range(T):
        R, C, A, B = list(map(int, input().split()))
        res = solve(R, C, A, B)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

