''' E - LCM on Whiteboard
https://atcoder.jp/contests/abc259/tasks/abc259_e
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
    N = int(input())

    A = []
    for _ in range(N):
        m = int(input())
        facs = [list(map(int, input().split())) for _ in range(m)]
        A.append(facs)

    # find all primes p s.t. only 1 ele of A contains p at max duplicity
    mx = {}
    for facs in A:
        for p, c in facs:
            if c > mx.get(p, [0, 0])[0]: mx[p] = [c, 0]
            if c == mx[p][0]: mx[p][1] += 1
    mx = {p: c for p, (c, c2) in mx.items() if c2 == 1}

    res = set()
    for facs in A:
        h = hash(tuple(p for p, c in facs if c == mx.get(p, 0)))
        res.add(h)

    print(len(res))



if __name__ == '__main__':
    main()

