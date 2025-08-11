''' Yet Another Contest 5 P2 - Big Score
https://dmoj.ca/problem/yac5p2
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

def solve(N, A, B, C):
    sa, sb, sc = sum(A), sum(B), sum(C)
    if sa == sb == sc:
        res = [''] * 3
        
        ls = [A, B, C]
        mxi = -1
        for i in range(3):
            if mxi == -1 or ls[mxi] < ls[i]:
                mxi = i
        res[mxi] = 'Josh'

        ls = [A[::-1], B[::-1], C[::-1]]
        mxi = -1
        for i in range(3):
            if mxi == -1 or ls[mxi] < ls[i]:
                mxi = i
        res[mxi] = 'Nils'

        for i in range(3):
            if res[i] == '':
                res[i] = 'Mike'
                break
    
    elif sa == sb:
        if A > B: res = ['Josh', 'Nils', 'Mike']
        else: res = ['Nils', 'Josh', 'Mike']
    elif sb == sc:
        if B > C: res = ['Mike', 'Josh', 'Nils']
        else: res = ['Mike', 'Nils', 'Josh']
    else:
        if C > A: res = ['Nils', 'Mike', 'Josh']
        else: res = ['Josh', 'Mike', 'Nils']

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        res = solve(N, A, B, C)
        print(*res)


if __name__ == '__main__':
    main()

