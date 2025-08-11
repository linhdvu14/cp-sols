''' C. Game with Reversing
https://codeforces.com/contest/1834/problem/C
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

def solve(N, A, B):
    even = sum(1 for a, b in zip(A, B) if a != b)
    odd = sum(1 for a, b in zip(A, B[::-1]) if a != b)
    if not even: return 0
    if not odd: return 2
    return min(
        even * 2 - (1 if even % 2 == 1 else 0),
        odd * 2 - (1 if odd % 2 == 0 else 0),
    )


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        B = input().decode().strip()
        res = solve(N, A, B)
        print(res)


if __name__ == '__main__':
    main()

