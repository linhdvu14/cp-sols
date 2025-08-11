''' E. Prefix Function Queries
https://codeforces.com/contest/1721/problem/E
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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc

class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------


def main():
    S = input().decode().strip()
    Q = int(input())

    # precompute for S
    N = len(S)
    lps = [0] * (N + 10)
    dfa = [[0] * (N + 10) for _ in range(26)]
    dfa[ord(S[0]) - ord('a')][0] = 1

    for i in range(1, N):
        for c in range(26):
            if c == ord(S[i]) - ord('a'):
                dfa[c][i] = i + 1
                lps[i] = dfa[c][lps[i - 1]]
            else:
                dfa[c][i] = dfa[c][lps[i - 1]]
    
    # append to lps/dfa for each query
    for _ in range(Q):
        T = input().decode().strip()
        M = len(T)

        for i in range(N, N + M):
            for c in range(26):
                if c == ord(T[i - N]) - ord('a'):
                    dfa[c][i] = i + 1
                    lps[i] = dfa[c][lps[i - 1]]
                else:
                    dfa[c][i] = dfa[c][lps[i - 1]]

        print(*lps[N:N + M]) 


if __name__ == '__main__':
    main()

