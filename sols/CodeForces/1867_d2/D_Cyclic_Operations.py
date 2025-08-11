''' D. Cyclic Operations
https://codeforces.com/contest/1867/problem/D
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


def solve(N, K, B):
    if K == 1: return all(i == b - 1 for i, b in enumerate(B))

    seen = [0] * N
    for i in range(N):
        if seen[i]: continue
        
        pos = {}
        while True:
            if i in pos and len(pos) - pos[i] != K: return False
            if seen[i]: break
            seen[i] = 1
            pos[i] = len(pos)
            i = B[i] - 1

    return True


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, K, B)
        print('YES' if res else 'NO')


if __name__ == '__main__':
    main()

