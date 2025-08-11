''' Palindrome Free Strings
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e
'''

from ctypes import Union
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

def solve(N, S):
    if N < 5: return True
    def is_palindome(s): return all(s[i] == s[-1-i] for i in range(len(s)//2))

    # gen cands for S[:5]
    cur = ['']
    for i in range(5):
        nxt = []
        tail = S[i] if S[i] != '?' else '01'
        for cand in cur:
            for t in tail:
                nxt.append(cand + t)
        cur = nxt
    cur = [cand for cand in cur if not is_palindome(cand)]

    # gen valid 5-window, check 6-window
    for i in range(5, N):
        if not cur: break
        nxt = []
        tail = S[i] if S[i] != '?' else '01'
        for cand in cur:
            for t in tail:
                if not is_palindome(cand + t) and not is_palindome(cand[1:] + t): 
                    nxt.append(cand[1:] + t)
        cur = nxt

    return len(cur) > 0



def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        S = input().decode().strip()
        out = 'POSSIBLE' if solve(N, S) else 'IMPOSSIBLE'
        print(f'Case #{i+1}: {out}')


if __name__ == '__main__':
    main()

