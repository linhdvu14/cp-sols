''' Grid Escape 
https://codingcompetitions.withgoogle.com/codejamio/round/0000000000050fc5/0000000000054e9c
'''

def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        R, C, K = stdin.readline().strip().split()
        R, C, K = int(R), int(C), int(K)

        if K == R*C - 1:
            print('Case #{}: {}'.format(t + 1, "IMPOSSIBLE"))
            continue

        print('Case #{}: {}'.format(t + 1, "POSSIBLE"))
        r, c = divmod(K, C)

        if C == 1:
            for _ in range(K):
                print('E')
            for i in range(R - K):
                if i == 0:
                    print('S')
                else:
                    print('N')
            continue

        for _ in range(r):
            print('E' * C)
        for i in range(R - r):
            if i == 0:
                if c != C - 1:
                    print('E'*(C-c-1) + 'W' + 'E'*c)
                else:
                    print('S' + 'E'*c)
            else:
                print('E'*(C-1) + 'W')
    
 
if __name__ == '__main__':
    main()