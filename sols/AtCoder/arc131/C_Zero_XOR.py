''' C - Zero XOR
https://atcoder.jp/contests/arc131/tasks/arc131_c
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# proof by induction
# N=1 -> win
# N=2 -> lose
# N=3 -> win
# N=4 -> win iff there's a 3-subset with xor 0, i.e. an element === xor(A)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    xor = 0
    for a in A: xor ^= a

    for a in A:
        if a == xor:
            print('Win')
            return
    
    print('Win' if N % 2 == 1 else 'Lose')
    

  

if __name__ == '__main__':
    main()

