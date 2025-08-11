''' H. Hot Black Hot White
https://codeforces.com/contest/1725/problem/H
'''

from inspect import trace
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

# Z = 0 -> (0, 0) same color
# Z = 1 -> (0, 1), (0, 2) same color
# Z = 2 -> (1, 1), (2, 2), (1, 2) same color

def solve(N, A):
    pos = [[] for _ in range(3)]
    for i, a in enumerate(A): pos[a % 3].append(i)

    res = [0] * N
    if len(pos[0]) <= N // 2:
        for i in pos[0]: res[i] = 1
        one = N // 2 - len(pos[0])
        for i in pos[1] + pos[2]:
            if not one: break 
            res[i] = 1
            one -= 1
        return 0, res
    
    for i in pos[1]: res[i] = 1
    for i in pos[2]: res[i] = 1
    for i in pos[0][:N // 2 - len(pos[1]) - len(pos[2])]: res[i] = 1
    return 2, res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    a, b = solve(N, A)
    print(a)
    print(*b, sep='')


if __name__ == '__main__':
    main()

