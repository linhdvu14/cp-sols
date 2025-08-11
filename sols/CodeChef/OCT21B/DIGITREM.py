''' Digit Removal

https://www.codechef.com/OCT21B/problems/DIGITREM

'''

def solve(N, D):
    sn, sd = str(N), str(D)
    N = len(sn)
    for i, s in enumerate(sn): 
        if s==sd:
            # x0yz -> x111
            if sd=='0': return int('1'*(N-i)) - int(sn[i:])

            # x8889yz -> (x+1)000000
            if sd=='9':  
                for j in range(i-1, -1, -1):
                    if sn[j] != '8': return int(str(int(sn[j])+1) + '0'*(N-j-1)) - int(sn[j:])
                return 10**N - int(sn)
            
            # Dyz -> (D+1)00
            return 10**(N-i-1) - (int(sn[i+1:]) if i+1 < N else 0)
    return 0


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N, D = map(int, stdin.readline().strip().split())
        out = solve(N, D)
        print(out)


if __name__ == '__main__':
    main()

