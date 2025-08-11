''' E. Rearrange Brackets
https://codeforces.com/contest/1821/problem/E
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

# match every bracket with its complement
# greedily put pair of longest distance together
def solve(K, S):
    dists, st = [], []
    for i, c in enumerate(S):
        if c == '(': 
            st.append(i)
        else:
            j = st.pop()
            dists.append((i - j - 1) // 2)
    
    dists.sort()
    if not K: return sum(dists)
    return sum(dists[:-K])


def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        S = input().decode().strip()
        res = solve(K, S)
        print(res)


if __name__ == '__main__':
    main()

