''' Training 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6
'''

def solve(n, p, s):
    s.sort()

    cur = mn = s[p-1]*p - sum(s[:p])
    for i in range(p, len(s)):
        cur = cur + (s[i] - s[i-1])*p + s[i-p] - s[i]
        mn = min(mn, cur)

    return mn


def main():
    from sys import stdin, stdout, stderr
    
    T = int(stdin.readline().strip())

    for t in range(T):
        n, p = list(map(int, stdin.readline().strip().split()))
        s = list(map(int, stdin.readline().strip().split()))
        out = solve(n, p, s)
        print('Case #{}: {}'.format(t+1, out))

 
if __name__ == '__main__':
    main()