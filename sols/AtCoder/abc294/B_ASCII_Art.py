''' B - ASCII Art
https://atcoder.jp/contests/abc294/tasks/abc294_b
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
    R, C = list(map(int, input().split()))
    res = []
    for _ in range(R):
        A = list(map(int, input().split()))
        A = ['.' if not a else chr(a - 1 + ord('A')) for a in A]
        res.append(''.join(A)) 
    return res



if __name__ == '__main__':
    res = main()
    print(*res, sep='\n')

