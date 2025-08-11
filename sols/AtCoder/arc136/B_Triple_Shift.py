''' B - Triple Shift 
https://atcoder.jp/contests/arc136/tasks/arc136_b
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

def merge(a, b):
    c, cnt = [], 0
    na, nb, ia, ib = len(a), len(b), 0, 0
    while ia < na and ib < nb:
        if a[ia] > b[ib]:
            c.append(b[ib])
            cnt += na - ia
            ib += 1
        else:
            c.append(a[ia])
            ia += 1
    if ia < na: c.extend(a[ia:])
    if ib < nb: c.extend(b[ib:])
    return c, cnt


def mergesort(A):
    '''return (sorted array, num orig inversions)'''
    if len(A) < 2: return A, 0
    mid = (len(A)+1) // 2
    a, ca = mergesort(A[:mid])
    b, cb = mergesort(A[mid:])
    c, cc = merge(a, b)
    return c, ca+cb+cc
    

def count_inv(A):
    '''return num inversions'''
    _, cnt = mergesort(A)
    return cnt


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    CA, CB = [0] * 5001, [0] * 5001
    for a in A: CA[a] += 1
    for b in B: CB[b] += 1

    if not all(a == b for a, b in zip(CA, CB)): return 'No'
    if any(c > 1 for c in CA): return 'Yes'

    idx = {}
    for i, b in enumerate(B): idx[b] = i
    A = [idx[a] for a in A]
    cnt = count_inv(A)
    return 'Yes' if cnt % 2 == 0 else 'No'


if __name__ == '__main__':
    out = main()
    print(out)

