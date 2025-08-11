''' Problem C2: Second Second Meaning
https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/C2
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

BITS = 7

def solve(N, S):
    start = '.' if S[0] == '-' else '-'
    res = []
    for m in range(1 << BITS):
        ms = ['.' if (m >> b) & 1 else '-' for b in range(BITS)]
        res.append(start + ''.join(ms))
        if len(res) == N - 1: break

    return res


def gen():
    import random
    random.seed(123)

    for _ in range(100):
        N = random.randint(1, 100)
        ln = random.randint(1, 100)
        c = ''.join(random.choice('.__') for _ in range(ln))
        res = solve(N, c)
        assert len(res) == len(set(res)) == N - 1
        assert all(1 <= len(c) <= 10 for c in res)
        
    print('tests passed')


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        S = input().decode().strip()
        res = solve(N, S)
        print(f'Case #{t+1}:')
        for r in res: print(r)


if __name__ == '__main__':
    main()

