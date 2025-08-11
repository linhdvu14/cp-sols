''' Draupnir 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122837
'''
from sys import stdin, stdout, stderr


def solve(s1, s2):
    r1, s1 = divmod(s1, 2**56)
    r2, s1 = divmod(s1, 2**28)

    r4, s2 = divmod(s2, 2**52)
    r5, s2 = divmod(s2, 2**42)
    r6, s2 = divmod(s2, 2**35)

    s1 -= r6*(2**9) + r5*(2**11) + r4*(2**14)
    r3 = s1//(2**18)

    return [r1,r2,r3,r4,r5,r6]

def query(n):
    print(n)
    stdout.flush()
    return int(stdin.readline().strip())

def submit(nums):
    print(' '.join(str(n) for n in nums))
    stdout.flush()
    return int(stdin.readline().strip())

def main():
    T, W = list(map(int,stdin.readline().strip().split()))

    for t in range(T):
        s1 = query(56)
        if s1 == -1: exit(1)

        s2 = query(210)
        if s2 == -1: exit(1)

        nums = solve(s1, s2)
        o = submit(nums)
        if o == -1: exit(1)

 
if __name__ == '__main__':
    main()
