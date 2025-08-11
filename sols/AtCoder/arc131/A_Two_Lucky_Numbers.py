''' A - Two Lucky Numbers
https://atcoder.jp/contests/arc131/tasks/arc131_a
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    A = input().decode().strip()    
    B = input().decode().strip()
    print(str(int(B + '0')//2) + A)
  

if __name__ == '__main__':
    main()

