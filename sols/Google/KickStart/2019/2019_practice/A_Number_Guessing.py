''' Number Guessing 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/00000000000588f4
'''
def main():
    from sys import stdin, stdout, stderr
    
    T = int(stdin.readline().strip())

    for t in range(T):
        A, B = stdin.readline().strip().split()
        A, B = int(A)+1, int(B)
        N = int(stdin.readline().strip())

        for _ in range(N):
            if A > B:
                break

            mid = A + (B-A) // 2
            print(mid)
            stdout.flush()
            
            result = stdin.readline().strip()

            if result == 'TOO_SMALL':
                A = mid+1
            elif result == 'TOO_BIG':
                B = mid-1
            elif result == 'CORRECT':
                break
            elif result == 'WRONG_ANSWER':
                exit(1)
    
 
if __name__ == '__main__':
    main()