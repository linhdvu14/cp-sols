''' Book Reading 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e02/000000000018fd0d
'''
def solve(n,m,q,ps,rs):
    valid = [True]*(n+1)
    for p in ps: valid[p] = False

    cnts = {}
    for r in rs:
        if r not in cnts: cnts[r] = 0
        cnts[r] += 1

    out = 0
    for k,v in cnts.items():
        r = k
        while r <= n:
            if valid[r]: out += v
            r += k
    return out


def main():
    from sys import stdin

    T = int(stdin.readline().strip())
    for t in range(T):
        n, m, q = list(map(int, stdin.readline().strip().split()))
        ps = list(map(int, stdin.readline().strip().split()))
        rs = list(map(int, stdin.readline().strip().split()))
        out = solve(n,m,q,ps,rs)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()