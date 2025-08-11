''' F - Spices
https://atcoder.jp/contests/abc236/tasks/abc236_f
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# relating XOR sums to vector space basis: https://codeforces.com/blog/entry/68953
# https://atcoder.jp/contests/abc236/submissions/28985124
# https://atcoder.jp/contests/abc236/submissions/28971561

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C = [(c, i+1) for i, c in enumerate(C)]
    C.sort()
    
    res = 0
    ok = [False] * (1 << N)
    ok[0] = True
    for c, v in C:
        # v can be obtained by some vals in basis set
        if ok[v]: continue

        # add v to basis set
        res += c
        for i in range(1 << N):
            if ok[i]:
                ok[i^v] = True

    print(res)


if __name__ == '__main__':
    main()

