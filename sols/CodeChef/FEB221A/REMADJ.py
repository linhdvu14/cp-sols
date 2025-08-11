''' Remove Adjacent
https://www.codechef.com/FEB221A/problems/REMADJ
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

# partition A into max number of intervals with same sum

def solve(N, A):
    S = sum(A)

    pref = [0]
    for a in A: pref.append(pref[-1] + a)

    pref_idx = {}
    for i, p in enumerate(pref):
        if p not in pref_idx: pref_idx[p] = []
        pref_idx[p].append(i)

    # check possible partition sums
    cc = 1
    checked = set()
    for i, p in enumerate(pref):
        if i == 0 or p in checked or (p == 0 and S != 0) or (p != 0 and S % p != 0): continue
        last, msz, sz = i-1, -1, 1
        while p * sz in pref_idx:
            idx = pref_idx[p * sz]
            found = False
            for j in idx:
                if j > last:
                    last = j
                    found = True
                    break
            if not found: break
            if pref[N] - pref[last] == 0: msz = sz
            sz += 1
        
        cc = max(cc, msz)
        checked.add(p)

    return N - cc


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

