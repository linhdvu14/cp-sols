''' C2. Dual (Hard Version)
https://codeforces.com/contest/1855/problem/C2
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
    mni = mxi = mxai = pos = neg = 0
    for i, a in enumerate(A):
        if a < A[mni]: mni = i
        if a > A[mxi]: mxi = i
        if abs(a) > abs(A[mxai]): mxai = i
        if a > 0: pos += 1
        elif a < 0: neg += 1
    
    if A[mxai] == 0: return []

    res = []
    all_pos = pos > 0
    if pos and neg: 
        if pos <= 7:  # 5 ops to create -20, 7 ops to make all neg
            all_pos = False
            while A[mni] > -20:
                A[mni] *= 2
                res.append([mni, mni])
            for i in range(N):
                if A[i] > 0:
                    A[i] += A[mni]
                    res.append([i, mni])
        elif neg <= 7:  # 5 ops to create 20, 7 ops to make all pos
            all_pos = True
            while A[mxi] < 20:
                A[mxi] *= 2
                res.append([mxi, mxi])
            for i in range(N):
                if A[i] < 0:
                    A[i] += A[mxi]
                    res.append([i, mxi])
        else:  # 12 ops to make same sign
            all_pos = A[mxai] > 0
            for i in range(N):
                if A[i] * A[mxai] >= 0: continue
                A[i] += A[mxai]
                res.append([i, mxai])
    
    # 19 ops to roll
    if all_pos:
        for i in range(N - 1):
            A[i + 1] += A[i]
            res.append([i + 1, i])
    else:
        for i in range(N - 1, 0, -1):
            A[i - 1] += A[i]
            res.append([i - 1, i])

    assert A == sorted(A)
    assert len(res) < 32
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(len(res))
        for a, b in res: print(a + 1, b + 1)

if __name__ == '__main__':
    main()
