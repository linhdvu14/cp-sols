''' F. Dasha and Nightmares
https://codeforces.com/contest/1800/problem/F
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

from random import randrange
class IntKeyDict(dict):
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]
    def pop(self, k): return super().pop(k^self.rand)


def main():
    N = int(input())

    sig, have = [0] * N, [0] * N
    for i in range(N):
        S = input().decode().strip()
        for c in S:
            c = ord(c) - ord('a')
            sig[i] ^= 1 << c
            have[i] |= 1 << c
    
    res = 0
    full = (1 << 26) - 1
    for c in range(26):
        tar = full ^ (1 << c)
        cands = [i for i, m in enumerate(have) if m & tar == m]
        cnt = IntKeyDict()
        for i in cands: 
            s = sig[i]
            res += cnt.get(s ^ tar, 0)
            cnt[s] = cnt.get(s, 0) + 1
    
    print(res)
        



if __name__ == '__main__':
    main()

