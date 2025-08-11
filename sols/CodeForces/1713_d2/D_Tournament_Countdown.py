''' D. Tournament Countdown
https://codeforces.com/contest/1713/problem/D
'''

# to test: 
# pypy3 template.py
# or: python3 interactive_runner.py python3 local_testing_tool.py 0 -- python3 a.py

import sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work

# -----------------------------------------

def ask(a, b):
    sys.stdout.write('? ' + str(a) + ' ' + str(b) + '\n')
    sys.stdout.flush()
    res = int(input())
    assert res != -1
    if res == 0: return -1
    if res == 1: return a
    return b


from collections import deque

# rm 2^n - 1 cands in 2^(n+1)/3 queries -> 2^(n+1) / 3 / 2^n = 2/3 queries to rm 1 cand = 2 queries to rm 3 cands
def solve():
    N = int(input())
    cands = deque(list(range(1, (1<<N) + 1)))
    while len(cands) > 1:
        a = cands.popleft()
        b = cands.popleft()
        if not cands: 
            cands.append(ask(a, b))
        else:
            c = cands.popleft()
            d = cands.popleft()
            w = ask(a, c)
            if w == -1: cands.append(ask(b, d))
            elif w == a: cands.append(ask(a, d))
            else: cands.append(ask(b, c))

    sys.stdout.write('! ' + str(cands[0]) + '\n')
    sys.stdout.flush()


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()