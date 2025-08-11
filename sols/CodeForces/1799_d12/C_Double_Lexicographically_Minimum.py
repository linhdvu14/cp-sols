''' C. Double Lexicographically Minimum
https://codeforces.com/contest/1799/problem/C
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

def solve(S):
    if len(S) == 1: return S 

    rem = sorted(list(S), reverse=True)
    half = []
    while len(rem) >= 2:
        a, b = rem.pop(), rem.pop()
        if a == b:
            half.append(a)
        else:
            n = len(rem) + 1
            if set(rem) == {b}:  # insert a to middle
                half += [b] * (n // 2)
                res = half + [b] * (n % 2) + [a] + half[::-1]
            else:
                res = half + [b] + rem[::-1] + [a] + half[::-1]
            return ''.join(res)
    
    res = half + rem + half[::-1]
    return ''.join(res)



def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        res = solve(S)
        print(res)


if __name__ == '__main__':
    main()

