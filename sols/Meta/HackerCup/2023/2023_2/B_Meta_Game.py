''' Problem B: Meta Game
https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/B
'''

import os, sys
input = sys.stdin.readline
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

def solve(N, A, B):
    def ok(shift):
        assert 0 <= shift < 2 * N
        if shift <= N:
            A2 = A[shift:] + B[:shift]
            B2 = B[shift:] + A[:shift]
        else:
            shift -= N 
            A2 = B[shift:] + A[:shift]
            B2 = A[shift:] + B[:shift]
        for i in range(N):
            if i < N // 2 and A2[i] >= B2[i]: return False 
            if i >= (N + 1) // 2 and A2[i] <= B2[i]: return False 
            if A2[i] != B2[-1 -i]: return False 
        return True
    
    eq = -1
    for i, (a, b) in enumerate(zip(A, B)):
        if a == b: 
            if eq != -1: return -1 
            eq = i 

    if N % 2:
        if eq == -1: return -1
        k = (eq - N // 2) % N
        for shift in [k, k + N]:
            if ok(shift): 
                return shift
        return -1
    
    else:
        if eq != -1: return -1

        pivot = -1
        for i in range(1, N):
            if (A[i] < B[i]) != (A[i - 1] < B[i - 1]):
                pivot = i 
                break
        
        if pivot == -1: 
            k = N // 2 if A[0] < B[0] else N // 2 + N
            return k if ok(k) else -1
        else:
            for i in range(pivot + 1, N):
                if (A[i] < B[i]) != (A[i - 1] < B[i - 1]):
                    return -1
            
            if A[0] < B[0]:
                k = pivot - N // 2 if pivot >= N // 2 else pivot + N // 2
                for shift in [k, k + N]:
                    if ok(shift): 
                        return shift
                return -1
            else:
                k = pivot + N // 2
                return k if ok(k) else -1


def gen():
    from collections import deque

    for N in range(2, 500):
        A = list(range(N))
        B = A[::-1]
        A, B = deque(A), deque(B)

        for shift in range(2 * N):
            got = solve(N, list(A), list(B))
            if got != shift:
                print(N)
                print(*A)
                print(*B)
                print(f'exp={shift}')
                print(f'got={got}')
                exit(1)
            A.appendleft(B.pop())
            B.appendleft(A.pop())

    print('tests passed')



def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, A, B)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()
    # gen()
