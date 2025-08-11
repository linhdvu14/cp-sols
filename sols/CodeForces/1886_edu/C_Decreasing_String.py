''' C. Decreasing String
https://codeforces.com/contest/1886/problem/C
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

def solve(S, pos):
    N = len(S)

    round = 0
    for i in range(N):
        if pos - (N - i) <= 0: break
        pos -= N - i
        round = i + 1
    
    removal = [-1] * N
    st, cnt = [], 0
    for i, c in enumerate(S):
        while st and S[st[-1]] > c: removal[st.pop()] = cnt = cnt + 1
        st.append(i)
    while st: removal[st.pop()] = cnt = cnt + 1

    for i, t in enumerate(removal):
        if t > round: pos -= 1
        if not pos: return S[i]


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        pos = int(input())
        res = solve(S, pos)
        print(res, end='')


if __name__ == '__main__':
    main()

