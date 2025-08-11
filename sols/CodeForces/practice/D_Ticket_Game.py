''' D. Ticket Game
https://codeforces.com/contest/1215/problem/D
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

# let A/B = min/max of S[:N//2+1] and S[N//2:], Na/Nb = num free slots in A/B
# sum(A) == sum(B):
#  * Na == Nb: Bob wins by mirroring Alice
#  * Na < Nb: Alice wins by playing 0 at A -> mirroring Bob -> playing nonzero at B
# sum(A) < sum(B):
#  * Na <= Nb: Alice wins by playing 0 at A -> mirroring Bob 
#  * Na > Nb: 
#      Alice plays (0 at A, 9 at B), Bob plays (9 at A, 0 at B) -> sum(B) - sum(A) unchanged for first 2*Nb rounds
#      if Na - Nb == 2, Bob wins iff sum(B) - sum(A) == 9
#      if Na - Nb == 2d, Bob wins iff sum(B) - sum(A) == 9*d

# also see https://codeforces.com/blog/entry/69815?#comment-543018

def solve(N, S):
    sa = sb = na = nb = 0
    for c in S[:N//2]:
        if c == '?': na += 1
        else: sa += int(c)
    for c in S[N//2:]:
        if c == '?': nb += 1
        else: sb += int(c)
    
    # if sa > sb or (sa == sb and na > nb): sa, sb, na, nb = sb, sa, nb, na 
    # if sa == sb and na == nb: return 'Bicarp'
    # if sa == sb and na < nb: return 'Monocarp'
    # if na <= nb: return 'Monocarp'
    if sb - sa == 9 * (na - nb) // 2: return 'Bicarp'
    return 'Monocarp'


def main():
    N = int(input())
    S = input().decode().strip()
    out = solve(N, S)
    print(out)


if __name__ == '__main__':
    main()

