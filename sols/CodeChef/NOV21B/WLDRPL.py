''' Wildcard Replacement
https://www.codechef.com/NOV21B/problems/WLDRPL
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def solve():
    S = input().decode().strip()
    N = len(S)
    Q = int(input())

    # MN[l] = min possible value for expression whose left parenthesis is at l
    # MX[l] = max possible value for expression whose left parenthesis is at l
    MN = [0]*N
    MX = [1]*N
    stack = []  # (l idx, op idx)
    for i, c in enumerate(S):
        if c == '(':
            stack.append([i, -1])
        elif c == '+' or c == '-':
            stack[-1][-1] = i
        elif c == ')':
            l, op = stack.pop()
            l1, l2 = l+1, op+1
            MN[l] = MN[l1] + MN[l2] if S[op] == '+' else MN[l1] - MX[l2]
            MX[l] = MX[l1] + MX[l2] if S[op] == '+' else MX[l1] - MN[l2]
    
    buff = []
    for _ in range(Q):
        l, r = tuple(map(int, input().split()))
        out = 1 if l == r else MX[l-1]
        buff.append(out)
    
    output(' '.join(map(str, buff)) + '\n')


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()

