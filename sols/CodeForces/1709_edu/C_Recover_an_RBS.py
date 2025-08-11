''' C. Recover an RBS
https://codeforces.com/contest/1709/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]


INF = float('inf')

# -----------------------------------------

# (((..))) is alwayas valid
# greedily swap last ( with first )

def solve(S):
    N = len(S)
    need_op = N // 2 - S.count('(')
    need_cl = N // 2 - S.count(')')
    if need_op == 0 or need_cl == 0: return 'YES'

    last_op = first_cl = -1
    for i, c in enumerate(S):
        if c != '?': continue
        if need_op: 
            S[i] = '('
            last_op = i
            need_op -= 1
        else:
            if first_cl == -1: first_cl = i
            S[i] = ')'

    S[last_op], S[first_cl] = ')', '('
    bal = 0
    for c in S:
        if c == '(': bal += 1
        else: bal -= 1
        if bal < 0: return 'YES'

    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        S = list(input().decode().strip())
        out = solve(S)
        print(out)


if __name__ == '__main__':
    main()

