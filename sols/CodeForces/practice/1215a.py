def solve(a1, a2, k1, k2, n):
    if k1 > k2: a1, a2, k1, k2 = a2, a1, k2, k1
    mn = max(0, n-(k1-1)*a1-(k2-1)*a2)
    mx = min(a1, n//k1) + (n - k1*min(a1, n//k1))//k2
    return mn, mx

def main():
    from sys import stdin
    
    a1, a2, k1, k2, n = [int(stdin.readline().strip()) for _ in range(5)]
    mn, mx = solve(a1, a2, k1, k2, n)
    print(mn, mx)

if __name__ == '__main__':
    main()