''' MEX-OR

https://www.codechef.com/OCT21B/problems/MEXOR

'''

# arr must contain consecutive integers, else arr'=1..(missing num) also <=N and has same MEX as arr
# let arr=1..X, then X must be all 1s, otherwise arr'=1..Y where Y = next all 1s >= X has same XOR and greater MEX
def solve(N):
    for i in range(32, -1, -1):
        mx = (1<<i) - 1 
        if mx <= N: 
            return mx+1


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

