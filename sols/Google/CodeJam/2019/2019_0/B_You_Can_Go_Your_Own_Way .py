''' You Can Go Your Own Way 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
'''

def solve(p):
    out = ''
    for c in p:
        out += 'E' if c == 'S' else 'S'
    return ''.join(out)


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        n = int(stdin.readline().strip())
        p = stdin.readline().strip()
        out = solve(p)
        print('Case #{}: {}'.format(t+1, out))
 
if __name__ == '__main__':
    main()