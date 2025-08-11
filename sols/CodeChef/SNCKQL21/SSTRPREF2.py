''' Prefix as a Substring 2
https://www.codechef.com/SNCKQL21/problems/SSTRPREF2
'''


import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def kmp(S):
    M = len(S)
    LPS = [0]*M  # LPS[i]==j ---> S[0..j-1]==S[i-j+1..i]
    j = 0        # end idx of current LPS candidate
    for i in range(1, M):
        while j > 0 and S[i] != S[j]:  # backtrack to find next longest LPS if needed
            j = LPS[j-1]
        if S[i] == S[j]:  # match -> increment i, j
            j += 1
        LPS[i] = j
    return LPS    


# Z[i] = max length d s.t. S2[i..i+d] == S1[0..d]
def zf(S1, S2):
    def _z(S):
        N = len(S)
        Z = [0]*N
        l = r = 0
        for i in range(1, N):
            if i <= r: 
                Z[i] = min(Z[i-l], r-i+1)
            while i+Z[i] < N and S[i+Z[i]] == S[Z[i]]: 
                Z[i] += 1
            if i+Z[i]-1 > r: 
                l, r = i, i+Z[i]-1
        return Z
    S = S1 + '$' + S2
    Z = _z(S)
    return Z[len(S1)+1:] + [0]


def solve(P, Q, X):
    LPS = kmp(P)
    Z = zf(Q, X)

    # iterate over X
    # for each longest matched prefix length pi of P (LPS)
    # store 1 + longest matched prefix length of Q (Z)
    mx = [0]*(len(P)+1)
    pi = 0  # index within P
    for xi in range(len(X)):  # index within X
        while pi > 0 and X[xi] != P[pi]:
            pi = LPS[pi-1]
        if X[xi] == P[pi]:
            pi += 1
        mx[pi] = max(mx[pi], Z[xi+1]+1)
        if pi == len(P):
            pi = LPS[pi-1]

    # if pppqqq is substring of X then ppqqq is also substring of X
    # propagate back
    mx[0] = max(mx[0], Z[0]+1)
    for i in range(len(mx)-1, 0, -1):
        prev = LPS[i-1]
        mx[prev] = max(mx[prev], mx[i])

    # combine
    return sum(mx)


def main():
    T = int(input())
    for _ in range(T):
        P = input().decode().strip()
        Q = input().decode().strip()
        X = input().decode().strip()
        out = solve(P, Q, X)
        print(out)


if __name__ == '__main__':
    main()

