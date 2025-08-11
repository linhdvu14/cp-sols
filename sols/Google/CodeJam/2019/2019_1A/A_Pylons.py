''' Pylons 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03
'''
def is_valid(r1, c1, r2, c2):
    return r1 != r2 and c1 != c2 and r1-c1 != r2-c2 and r1+c1 != r2+c2


def solve_random(nr, nc):
    res = []
    while not res: res = _solve_random(nr, nc)
    for r, c in res:
        print('{} {}'.format(r+1, c+1))


def _solve_random(nr, nc):
    import random
    rem = set((r, c) for r in range(nr) for c in range(nc))

    r1, c1 = random.choice(list(rem))
    rem.remove((r1,c1))
    res = [(r1,c1)]

    while rem:
        r2, c2 = random.choice(list(rem))
        tried = set((r2,c2))
        while not is_valid(r1,c1,r2,c2):
            r2, c2 = random.choice(list(rem))
            tried.add((r2,c2))
            if len(tried) >= len(rem): 
                return []
        res.append((r2,c2))
        rem.remove((r2,c2))
        r1, c1 = r2, c2

    return res



def solve(nr, nc):
    return solve_random(nr, nc)


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        nr, nc = list(map(int,stdin.readline().strip().split()))
        if (nr,nc) in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:
            print('Case #{}: {}'.format(t+1, 'IMPOSSIBLE'))
        else:
            print('Case #{}: {}'.format(t+1, 'POSSIBLE'))
            solve(nr, nc)

 
if __name__ == '__main__':
    main()