''' D. Array Painting
https://codeforces.com/contest/1849/problem/D
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

def solve(N, A):
    blocks = []
    pa, cnt = A[0], 0
    for a in A:
        if (a == 0 and pa > 0) or (a > 0 and pa == 0):
            blocks.append([pa, cnt])
            pa = a 
            cnt = 1
        else:
            if pa > 0: pa = max(pa, a)
            cnt += 1
    blocks.append([pa, cnt])

    res = 0
    for i, (a, _) in enumerate(blocks):
        if a == 2:
            res += 1
            if i and blocks[i - 1][1]: blocks[i - 1][1] -= 1
            if i + 1 < len(blocks) and blocks[i + 1][1]: blocks[i + 1][1] -= 1    
    for i, (a, _) in enumerate(blocks):
        if a == 1:
            res += 1
            if i and blocks[i - 1][1]: blocks[i - 1][1] -= 1
            elif i + 1 < len(blocks) and blocks[i + 1][1]: blocks[i + 1][1] -= 1
    for i, (a, cnt) in enumerate(blocks):
        if a == 0:
            res += cnt

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    print(res)


if __name__ == '__main__':
    main()

