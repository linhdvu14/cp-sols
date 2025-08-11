''' Cheerio Contest 3 P3 - Everything Array
https://dmoj.ca/problem/cheerio3p3
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

#          1, 2, ..., k |           x           |            y
# covers   [1, 2k - 1]  | [x - k, x + k] \ {x}  | [y - k, y + k] \ {y}
# want 
# - x + k + 1 = y - k -> y - x = 2k + 1
# - set x = 2k + 1

# ---> 1, 2, ..., k | 2k + 1 | 2(2k + 1) | ... | n(2k + 1)
# can cover 1 .. n(2k + 1) + k except n(2k + 1)
# want n(2k + 1) + k >= N -> n = ceil((N - k) / (2k + 1))

# e.g. k = 5: 1, 2, 3, 4, 5 |         11        |     22             |      33
#               [1, 9]      |  [6, 16] \ {11}   |  [17, 27] \ {22}   | [28, 38] \ {33}

def solve(N, M):
    bound = int((N * 2) ** 0.5)
    for k in range(3, bound + 1):
        d = 2 * k + 1
        n = (N - k + d - 1) // d 
        cand = list(range(1, k + 1)) 
        for i in range(1, n + 1): cand.append(d * i)
        if cand[-1] > N:
            cand.pop()
            x = cand[-1] + k 
            if x < N: cand.append(x)  # cover till x + 2k

        if len(cand) <= M: return cand


def main():
    N, M = list(map(int, input().split()))
    res = solve(N, M)
    print(len(res))
    print(*res)


if __name__ == '__main__':
    main()

