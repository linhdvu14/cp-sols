''' C - kasaka
https://atcoder.jp/contests/abc237/tasks/abc237_c
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

def main():
    S = input().decode().strip()
    N = len(S)

    l, r = 0, N-1
    while l < N and S[l] == 'a': l += 1
    while r >= 0 and S[r] == 'a': r -= 1

    if l > N-1-r: return 'No'
    
    while l <= r:
        if S[l] != S[r]: return 'No'
        l += 1
        r -= 1
    
    return 'Yes'



if __name__ == '__main__':
    out = main()
    print(out)

