''' H-index 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edd/00000000001a274e
'''
MAX = 10**5 + 1

def solve(n, nums):
    counts = [0]*MAX
    total = 0
    h = 0
    out = []

    for i, num in enumerate(nums):
        counts[num] += 1
        if num >= h+1: total += 1
        if total >= h+1:
            total -= counts[h+1]
            h += 1
        out.append(h)

    return out


def main():
    from sys import stdin

    T = int(stdin.readline().strip())
    for t in range(T):
        n = int(stdin.readline().strip())
        nums = list(map(int, stdin.readline().strip().split()))
        out = solve(n, nums)
        print('Case #{}: {}'.format(t+1, ' '.join(map(str,out))))


if __name__ == '__main__':
    main()