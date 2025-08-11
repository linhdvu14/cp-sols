''' C. Queries for the Array
https://codeforces.com/contest/1861/problem/C
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
    st = []
    zero = 0
    for c in S:
        if c == '+': 
            st.append(-1)
        elif c == '-': 
            v = st.pop()
            if v == 0: zero -= 1
            if v == 1 and st: st[-1] = 1
        elif c == '0':
            if len(st) < 2 or st[-1] == 1: return 'NO'
            if st[-1] == -1:
                st[-1] = 0
                zero += 1
        else:
            if zero: return 'NO'
            if st: st[-1] = 1
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        res = solve(S)
        print(res)


if __name__ == '__main__':
    main()
