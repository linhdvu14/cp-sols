''' Golf Gophers 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104f1a
'''
def solve(d,m):
    for num in range(1,m+1):
        if all(num % k == v for k,v in d.items()):
            return num
    return -1



def main():
    from sys import stdin, stdout, stderr
    
    T, n, m = list(map(int,stdin.readline().strip().split()))
    primes = [5,7,9,11,13,16,17]

    for t in range(T):
        d = {}
        for i in range(min(n,len(primes))):
            print(' '.join(str(primes[i]) for _ in range(18)))
            stdout.flush()
            d[primes[i]] = sum(list(map(int,stdin.readline().strip().split()))) % primes[i]

        print(solve(d,m))
        stdout.flush()
        if stdin.readline().strip() == '-1': exit(1)
    
 
if __name__ == '__main__':
    main()