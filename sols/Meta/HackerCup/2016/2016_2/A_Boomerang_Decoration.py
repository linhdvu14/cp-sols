''' Problem A: Boomerang Decoration
https://www.facebook.com/codingcompetitions/hacker-cup/2016/round-2/problems/A
'''

INF = float('inf')

def solve(N, A, B):
    A = [ord(c) - ord('A') + 1 for c in A]
    B = [ord(c) - ord('A') + 1 for c in B]
    
    # dp_left[i][s] = min steps to paint A[:i] where
    # s = 0: all letters are original
    # s > 0: all letters are s
    dp_left = [[INF]*27 for _ in range(N+1)]
    for s in range(27):
        dp_left[0][s] = 0

    for i in range(1,N+1):
        for s in range(27):
            if (s==0 and A[i-1]==B[i-1]) or s==B[i-1]:  # no need to paint A[i-1]
                dp_left[i][s] = dp_left[i-1][s]
            else:
                dp_left[i][s] = 1 + dp_left[i-1][B[i-1]]

    # dp_right[i][s] = min steps to paint A[i:] where
    # s = 0: all letters are original
    # s > 0: all letters are s
    dp_right = [[INF]*27 for _ in range(N+1)]
    for s in range(27):
        dp_right[N][s] = 0

    for i in range(N-1,-1,-1):
        for s in range(27):
            if (s==0 and A[i]==B[i]) or s==B[i]:
                dp_right[i][s] = dp_right[i+1][s]
            else:
                dp_right[i][s] = 1 + dp_right[i+1][B[i]]

    # try all possible splits
    res = N
    for i in range(N+1):
        l, r = dp_left[i][0], dp_right[i][0]
        res = min(res, max(l, r))
    
    return res


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for t in range(T):
        N = int(stdin.readline().strip())
        A = stdin.readline().strip()
        B = stdin.readline().strip()
        out = solve(N, A, B)
        print(f'Case #{t+1}: {out}')

if __name__ == '__main__':
    main()
