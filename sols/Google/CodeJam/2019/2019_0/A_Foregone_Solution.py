''' Foregone Solution 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
'''

def solve(n):
    a = b = ''
    for c in str(n):
        if c != '4':
            a += c
            b += '0'
        else:
            a += '2'
            b += '2'

    return int(a), int(b)


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        n = int(stdin.readline().strip())
        a, b = solve(n)
        print('Case #{}: {} {}'.format(t+1, a, b))
 
if __name__ == '__main__':
    main()