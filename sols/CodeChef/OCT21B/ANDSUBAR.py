'''  Longest AND Subarray

https://www.codechef.com/OCT21B/problems/ANDSUBAR

'''

def solve(N):
    res = 0
    for msb in range(32, -1, -1):
        if (N >> msb) & 1 == 1:  
            res = 1 + (N^(1<<msb))                   # 2^msb .. N
            if msb>0: res = max(res, (1<<(msb-1)))   # 2^(msb-1) .. 2^(msb-1) - 1
            break
    return res


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

