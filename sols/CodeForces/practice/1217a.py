def solve(s, i, e):
    mx = s + e
    mn = max(s, (s+i+e)//2 + 1)
    if mn > mx: return 0
    return mx-mn+1


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        s, i, e = list(map(int,stdin.readline().strip().split()))
        print(solve(s,i,e))
 
if __name__ == '__main__':
    main()