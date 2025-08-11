''' C. Jatayu's Balanced Bracket Sequence
https://codeforces.com/contest/1726/problem/C
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

# sibling RBS on same level are connected
# each ( adds 1 if it's the first child
# inp: [ ( ( ( ) ( ) ) ( ) ) ]
# bal: 0 1 2 3 . 3 . . 2 . . .
# add:   + + +

def solve_1(N, S):
    res = cur = prev = 0
    for c in S:
        if c == '(': 
            cur += 1
            if cur > prev: res += 1
            prev = cur
        else: 
            cur -= 1

    return res


def solve_2(N, S):
    res = 1
    for i in range(1, 2 * N):
        if S[i] == S[i - 1] == '(': 
            res += 1
    return res


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        res = solve(N, S)
        print(res)


if __name__ == '__main__':
    main()

