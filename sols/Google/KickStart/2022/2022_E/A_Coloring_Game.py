''' Coloring Game 
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba856a
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

def solve(N):
    return (N + 4) // 5


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        out = solve(N)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

